# youtube-trends-spider
crawler youtube trends use selenium on python<br>
抓取 Youtube 近期觀看、分享次數熱門影片<br>
抓取使用<b> JavaScript </b>或<b> AJAX </b>生成的網頁
* [Demo Video待新增]() - Windows 

## 特色
* 抓取 Youtube 近期觀看、分享次數熱門影片([目標頁面](https://www.youtube.com/trendsdashboard#loc0=twn&age0=--))，並輸出SQLITE檔案。
* 抓取使用<b> JavaScript </b>或<b> AJAX </b>生成的網頁資料。
   
## 安裝套件
由於 trends_selenium.py 有使用到 Selenium，所以須先安裝 Selenium，<br>
安裝方法 :<br>
```
pip install selenium 
```
更多詳細資料可參考 [Selenium 文件](http://selenium-python.readthedocs.org/#)

## 執行範例 
<b> trends.py </b> 和 <b> trends_selenium.py </b> 所得到的結果是相同的，只是使用的方法不同。<br>
<b> trends.py </b> 直接從 API 獲取資料 (抓取速度快)
```
python trends.py
```
<b> trends_selenium.py </b> 使用 selenium 獲取資料 (抓取速度會比較慢，因為是模擬整個瀏覽器)
```
python trends_selenium.py 
```

## 執行過程
trends.py<br>
![alt tag](http://i.imgur.com/qxPR9yd.jpg)

trends_selenium.py <br>
透過 Selenium 模擬瀏覽器，背景會自動開啟瀏覽器
![alt tag](http://i.imgur.com/bOgPiK3.jpg)

## 輸出格式
SQLITE<br>
![alt tag](http://i.imgur.com/jMuVSRi.jpg)
![alt tag](http://i.imgur.com/Md9aOaB.jpg)
內容
```
ID          排名
title       標題
link        標題link
autor_name  作者頻道
autor_link  作者頻道link      
views       觀看次數    
```

## 其他說明
trends.py 使用的目標網站連結
```
觀看次數最多
全部   https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=views&loc=twn&gender=--&age=-- 	       		  
男性   https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=views&loc=twn&gender=male&age=--	       		   
女性   https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=views&loc=twn&gender=female&age=--	       
  
分享次數
全部   https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=shared&loc=twn&gender=--&age=--		   		  
男性   https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=shared&loc=twn&gender=male&age=--	       		   
女性   https://www.youtube.com/trendsdashboard_ajax?action_feed_videos=1&feed=shared&loc=twn&gender=female&age=--
```
<br>
trends_selenium.py 使用的目標網站連結	
```
觀看次數最多
全部   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--
男性   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&gen0=male
女性   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&gen0=female
  
分享次數
全部   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared
男性   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared&gen0=male
女性   https://www.youtube.com/trendsdashboard#loc0=twn&age0=--&feed=shared&gen0=female
``` 

## 執行環境
* Selenium 2.53.1
* Windows 8.1
* Python 2.7.3

## License
[MIT license](https://github.com/twtrubiks/youtube-trends-spider/blob/master/LICENSE)
