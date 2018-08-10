# Goal:
write an efficient crawling architecture and a query interface that gets the best selling products from yahoo store: 
* An efficient crawler to get product pricing and category information
* Define and discover how to get the best selling products, explain possible limitations
* A query interface to operate on crawled data, could be command line tools 
* Able to export result in CSV and excel

# Website:
* https://tw.buy.yahoo.com/
* 推薦的api 
https://tw.buy.yahoo.com/catalog/ajax/recmdHotNew

* 全站分類
https://tw.buy.yahoo.com/help/helper.asp?p=sitemap

* 分類頁
https://tw.buy.yahoo.com/?z=7&sort=-ptime&pg=1

# Usage:
## Install
* pip install -r requirements.txt
* Python version = 2.7.10

## Excute
python yahoo_buy_crawler.py

## Output data
data/

# Limitation:
* We can only query TOP 10 best seller categories from API.
* We can only query TOP 5 best seller item in a category from API.

# Design and Implement Steps: 
## Program Flow 
## Parse website
