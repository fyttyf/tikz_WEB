#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:09:05 2019

TODO:
    在compile下面都建立一个名字的目录
    复制到指定目录
    compile

    
@author: fengyutian
"""

import json
import os
import shutil

src_prefix = './data/examples/'

with open('./data/exampleName.json', 'r') as f:
    data = json.load(f)
    names = data['names']
    for i in range(len(names)):
        names[i] = names[i].split('.')[0]
        #print(names[i])
        #assert(1==0)
    
def moveFileto(sourceDir,  targetDir): 
    shutil.copy(sourceDir,  targetDir)   

def make_my_dir(nameList):
    dir_prefix = './data/compile/'
    for name in nameList:
        print(name)
        #assert(1==0)
        dir = dir_prefix + name
        src = src_prefix + name + '.tex'
        os.makedirs(dir, exist_ok=True)
        moveFileto(src, dir)
        
def my_compile(nameList):
    for name in nameList:
        print("#############"+ name)
        command = 'sh run_compile.sh '+name
        os.system(command)


#make_my_dir(names)
#my_compile(names)
        
#my_compile(names[0:100])
#my_compile(names[100:200])
#my_compile(names[200:300])
#my_compile(names[300:400])
my_compile(names[400:])

    
