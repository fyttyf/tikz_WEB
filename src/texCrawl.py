#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 21:23:55 2019

@author: fengyutian
"""
import json
import requests


with open('exampleName.json', 'r') as f:
    data = json.load(f)
    names = data['names']

url_prefix="http://www.texample.net/media/tikz/examples/TEX/"
path_prefix="./examples/"

for name in names:
    #print(name)
    #assert(1==0)
    
    url = url_prefix + name
    r=requests.get(url)
    print(name + " ok")
    
    path = path_prefix + name
    with open(path,"wb") as f:
        f.write(r.content)
    f.close()
    
