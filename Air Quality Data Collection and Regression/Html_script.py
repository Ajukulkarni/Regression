# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 00:06:53 2021

@author: ajitk
"""

import os
import time
import requests
import sys

os.getcwd()

def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month<10):
                url = "https://en.tutiempo.net/climate/0{}-{}/ws-432950.html".format(month,year)
            else:
                 url = "https://en.tutiempo.net/climate/{}-{}/ws-432950.html".format(month,year)
                 
            texts = requests.get(url)
            text_utf = texts.text.encode('utf=8')
        
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
        sys.stdout.flush()
        

if __name__=="__main__":
    start_time = time.time()
    retrieve_html()
    stop_time= time.time()
    print("Time taken {}".format(stop_time-start_time))