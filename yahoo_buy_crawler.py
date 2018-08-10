#!/usr/bin/env python
import json
import re
import selenium
import csv
import pandas as pd
import requests as r
from bs4 import BeautifulSoup as bs 

def export_to_file(data, out_filename):


    return

def query_from_cmd(yahoo_url):
    #subId = [1,999]
    #data_dict.keys()
    column_name = ["timestamp", "name", "price", "category_id", "category_name"]
    data_dict = {}
    cat_id_name_map = {}

    #Load URL
    content = json.loads(r.get(yahoo_url).text, encoding="utf-8")

    #Get (hpp) category id name map
    for i in content['billboard']['tabs']:
        cat_id_name_map[i["hpp"]] = i["label"]
    for i in content['billboard']['othertab']:
        cat_id_name_map[i["hpp"]] = i["label"]

    print "cat_id_name_map:\n%s" %cat_id_name_map

    return data_dict

def main():
    yahoo_url = 'https://tw.buy.yahoo.com/catalog/ajax/recmdHotNew'
    out_filename = ''

    #while(input_line):
    data = query_from_cmd(yahoo_url)
    export_to_file(data, out_filename)


if __name__ == '__main__':
    main()

