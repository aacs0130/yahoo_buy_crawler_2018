#!/usr/bin/env python
import time
import json
import re
import selenium
import unicodecsv as csv
#import csv
import pandas as pd
import requests as r
from bs4 import BeautifulSoup as bs 

def export_to_file(data, out_filename):
    head = u'timestamp, pd_id, name, price, cat_id, cat_name'
    timestamp = data[0][0]
    filename = "%s_%s.csv" %(out_filename, timestamp)
    txtfile = "%s_%s.txt" %(out_filename, timestamp)

    '''
    with open(filename, 'wb') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(head)
        for i in range(len(data)):
            wr.writerow(data[i])
    '''

    with open(txtfile, 'wb', 'utf-8') as myfile:
        myfile.write(head)
        for i in range(len(data)):
            myfile.write(data[i])

    return

def query_from_cmd(yahoo_url):
    #subId = [1,999]
    column_name = ["timestamp", "name", "price", "cat_id", "cat_name"]
    data_list = []
    cat_id_name_map = {}

    #Load URL
    content = json.loads(r.get(yahoo_url).text, encoding="utf-8")

    #Get timestamp
    timestamp = int(time.time())

    #Get (hpp) category id name map
    for i in content['billboard']['tabs']:
        cat_id_name_map[i["hpp"]] = i["label"]
    for i in content['billboard']['othertab']:
        cat_id_name_map[i["hpp"]] = i["label"]

    #print "cat_id_name_map:\n%s" %cat_id_name_map

    for i in range(10):
        item = content['billboard']['panels'][i]["mainitem"]
        pd_id = item["pdid"]
        hpp = item["hpp"]
        cat_id = hpp.split("_item")[0]
        cat_name = cat_id_name_map[cat_id]
        name = item["desc"]
        text_price = item["price"]
        haha = text_price.split('<')
        price = haha[len(haha)-2].split('>')[1]
        data_list.append("%s, %s, %s, %s, %s, %s " %
                (timestamp, pd_id, name, price, cat_id, cat_name))
        
    
        print "%d: %s" % (i,data_list)


    return data_list

def main():
    yahoo_url = 'https://tw.buy.yahoo.com/catalog/ajax/recmdHotNew'
    out_filename = 'data/yahoo_best_sell'

    #while(input_line):
    data = query_from_cmd(yahoo_url)
    export_to_file(data, out_filename)


if __name__ == '__main__':
    main()

