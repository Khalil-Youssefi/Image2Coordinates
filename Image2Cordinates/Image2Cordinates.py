# -*- coding: utf-8 -*-
"""
Created on Mon May 10 07:04:20 2021

@author: KH4LI
"""

import cv2

img = cv2.imread('map.png')
xys = []
w = len(img)
h = len(img[0,:])
for i in range(w):
    for j in range(h):
        if img[i,j,0] == 0:
            xys.append(str(i) + "\n")
            xys.append(str(j) + "\n")
f = open('map.txt','w')
f.writelines(xys)
f.close()