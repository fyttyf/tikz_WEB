#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:27:25 2019

@author: fengyutian
"""

import json


def save_tags(tags):
    d = {}
    d['tags'] = tags
    with open('./data/allTag.json', 'w') as f:
        json.dump(d, f)

with open('./data/exampleName.json', 'r') as f:
    data = json.load(f)
    names = data['names']


allTags = set()
path_prefix = './data/examples/'

for name in names:
    print(name)
    
    path = path_prefix + name 
    
    f = open(path,'r')
    lines = f.readlines()
    for line in lines:
       if "Tags:" in line:
         line = line.replace(':','')
         line = line.replace('Tags','')
         line = line.replace(',',';')
         line = line.strip()
         tags = line.split(';')
         for tag in tags:
             tag = tag.strip()
             allTags.add(tag)
             #print(tag)
         break;

save_tags(list(allTags))
  
