# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 19:24:34 2017

@author: Administrator
"""


import requests
import json
import time

url = 'https://s.taobao.com/search?spm=a230r.1.14.44.ebb2eb2O5dQpJ&type=samestyle&app=i2i&rec_type=1&uniqpid=-1071368795&nid=546459849736&sort=credit-desc&qq-pf-to=pcqq.c2c'

response = requests.get(url)

allText = response.text

jsonText = allText[allText.index('g_page_config')+16:allText.index('g_srp_loadCss')-6]
json_str = json.loads(jsonText)

goods = json_str["mods"]["recitem"]["data"]["items"]

goodList = []

for good in goods:
    
    thisList = []
    thisList.extend(good["dsr_scores"])
    thisList.append(good["nick"])
    thisList.append(good["item_loc"])
    thisList.append(good["view_sales"])
    thisList.append(good["title"])
    thisList.append(good["view_price"])
    thisList.append(good["comment_count"])
    thisList.append(good["view_fee"])
    
    iconList = ''
    for icon in good["icon"]:
        iconList += icon["innerText"]+'&'
    
    thisList.append(iconList)
    
    goodList.append(thisList)
    
today = time.strftime('%Y-%m-%d',time.localtime(time.time()))

with open('E:\GitHub\TaoBao\goodlist_'+today+'.txt','w') as fo:
    fo.write('如实描述\t')
    fo.write('服务态度\t')
    fo.write('物流服务\t')
    fo.write('店铺\t')
    fo.write('位置\t')
    fo.write('付款人数\t')
    fo.write('商品名称\t')
    fo.write('价格\t')
    fo.write('评价数\t')
    fo.write('运费\t')
    fo.write('标记\n')
    
    for mylist in goodList:
        fo.write('\t'.join(mylist))
        fo.write('\n')
