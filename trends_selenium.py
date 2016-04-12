#coding=utf-8
import sys
import os
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

filename = "youtube_trends_selenium.db"

#移除特殊字元
def remove(value, deletechars):
    for c in deletechars:
        value = value.replace(c,'')
    return value.rstrip();

def crawler(browser, table):  
    delay = 5 # seconds
    # selenium Wait 用法，可參考 http://selenium-python.readthedocs.org/en/latest/waits.html
    try:
      # 當 javascript or ajax 執行完畢時，在 <div id="videos-0-items">底下，會出多 class = "video-item"
      WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "video-item")))
      # 將資料餵給 BeautifulSoup
      soup = BeautifulSoup(browser.page_source,'html.parser')  
      # 開始分析 抓取資料
      for info in soup.select('.video-item-info') :
          # title
          title = info.select('h4 a')[0].text
          title = remove(title, "\"'") 
          # link
          link = "https://www.youtube.com" + info.select('h4 a')[0]["href"]
          # autor_name
          autor_name = info.select('a')[1].text
          autor_name = remove(autor_name, "\"'") 
          # autor_link
          autor_link = "https://www.youtube.com" + info.select('a')[1]['href']  
          # watch            
          watch = info.text
          startIndex = watch.find(u'觀看次數')
          watch = watch[startIndex:].strip()                           
          '''
          print "title:", title.encode(sys.getfilesystemencoding())
          print "link:", link.encode(sys.getfilesystemencoding())
          print "autor_name:", autor_name.encode(sys.getfilesystemencoding())
          print "autor_link:", autor_link.encode(sys.getfilesystemencoding())              
          print "watch:", watch.encode(sys.getfilesystemencoding())                    
          print "======================="      
          '''        
          # 連接資料庫
          conn = sqlite3.connect(filename)         
          with conn:
               cursor = conn.cursor()
               sql = 'create table if not exists ' + table + '(Id INTEGER PRIMARY key autoincrement, title TEXT, link TEXT, autor_name TEXT, autor_link TEXT, views TEXT )'
               cursor.execute(sql)
               # INSERT INTO table VALUES(NULL,'title','link','autor_name','autor_link','watch')
               sql = "INSERT INTO "+ table +" VALUES(NULL,\'"+ title +"\',\'"+ link +"\',\'"+ autor_name +"\',\'"+ autor_link +"\',\'"+ watch +"\')"                
               try:
                 cursor.execute(sql)
               except:
                 print 'Write SQLite error:', sql.encode(sys.getfilesystemencoding())           
    except TimeoutException:
      print "Loading took too much time!" 
          
def main():   
    
    links = [("https://www.youtube.com/trendsdashboard#loc0=twn&age0=--", "views_all"),
             ("https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&gen0=male", "views_male"),
             ("https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&gen0=female", "views_female"),
             ("https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared", "shared_all"),
             ("https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared&gen0=male", "shared_male"),
             ("https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared&gen0=female", "shared_female")
    ]

    '''
    觀看次數最多
    全部   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--
    男性   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&gen0=male
    女性   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&gen0=female
  
    分享次數
    全部   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared
    男性   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared&gen0=male
    女性   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared&gen0=female
    '''   
    
    # 如果資料庫已經存在則移除
    if os.path.exists(filename):
        os.remove(filename)
        
    count = 0
    print u'Start parsing... ' 
    
    browser = webdriver.Firefox()
    for link in links:
        count += 1
        # link[0] = URL   link[1] = tag    
        browser.get(link[0])
        browser.refresh()
        crawler(browser, link[1])
        print u"download: " + str(100 * count / len(links) ) + " %."
    browser.quit()
    print 'Completed' 
    
if __name__ == "__main__": 
   main() 
   