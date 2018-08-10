#!/usr/bin/env python
import json
import re
import selenium
import csv
import pandas as pd
import requests as rs
from bs4 import BeautifulSoup as bs 

def get_data_from_url():

def export_to_file():

def query_from_cmd():
    #subId = [1,999]
    df = get_data_from_url(yahoo_url)

def main():
    yahoo_url = ''
    out_filename = ''
    input_line = ''
    subId = 1

    #while(input_line):
    data = query_from_cmd(yahoo_url, subId)
    export_to_file(data, out_filename, subId)


if __name__ == '__main__':
    main()

