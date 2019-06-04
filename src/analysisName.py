#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 21:06:42 2019

@author: fengyutian
"""

# coding: UTF-8
'''
import requests
url="http://www.texample.net/media/tikz/examples/TEX/3d-cone.tex"
path="3d-cone.tex"
r=requests.get(url)
print("ok")
with open(path,"wb") as f:
    f.write(r.content)
f.close()
'''

from urllib.request import urlopen#用于获取网页
from bs4 import BeautifulSoup#用于解析网页
import json

def save_names(names):
    d = {}
    d['names'] = names
    with open('exampleName.json', 'w') as f:
        json.dump(d, f)
    
    
names = []

html = urlopen('http://www.texample.net/media/tikz/examples/TEX/')
bsObj = BeautifulSoup(html, 'html.parser')
t1 = bsObj.find_all('a')
for t2 in t1:
    t3 = t2.get('href')
    names.append(t3)
names = names[5:]
save_names(names)
    
