# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 12:59:32 2018

@author: Admin
"""

import os, glob

rootDir = input("Directory to parse: ")
os.chdir(rootDir)


for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        os.rename(os.path.join(dirName, fname), os.path.join(dirName,((fname[:-9])+'.full.jpg')))

