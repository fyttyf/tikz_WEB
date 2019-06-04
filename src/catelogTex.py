#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:59:25 2019

@author: fengyutian
"""

import json

with open('./data/allTag.json', 'r') as f:
    data_tag = json.load(f)
    tags = data_tag['tags']
    
with open('./data/exampleName.json', 'r') as f:
    data = json.load(f)
    names = data['names']
    
my_dict = dict.fromkeys(tags)

for key in my_dict:
    my_dict[key] = []



path_prefix = './data/examples/'
for name in names:
    path = path_prefix + name 
    f = open(path,'r')
    lines = f.readlines()
    for line in lines:
        if "Tags:" in line:
            #print(line)
            for tag in tags:
                if tag in line:
                    #print(tag)
                    #assert(1==0)
                    my_dict[tag].append(name)
            break
        
json_str = json.dumps(my_dict)
with open('./data/texCatelog.json', 'w') as json_file:
    json_file.write(json_str)