# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 19:24:34 2017

@author: Administrator
"""


import requests
import json

url = 'https://s.taobao.com/search?spm=a230r.1.14.44.ebb2eb2O5dQpJ&type=samestyle&app=i2i&rec_type=1&uniqpid=-1071368795&nid=546459849736&sort=credit-desc&qq-pf-to=pcqq.c2c'

response = requests.get(url)

allText = response.text

jsonText = allText[allText.index('g_page_config')+16:allText.index('g_srp_loadCss')-6]

#print(jsonText)

print(type(jsonText))

json_str = json.loads(jsonText)

print(type(json_str))

goods = json_str["mods"]["recitem"]["data"]["items"]

for good in goods:
    print(good["dsr_scores"])