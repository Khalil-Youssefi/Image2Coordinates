# -*- coding: utf-8 -*-
"""
Created on Mon May 10 07:04:20 2021

@author: KH4LI
"""

import cv2
import os

mapfile = input("Map file? ")
img = cv2.imread(mapfile);
if img is None:
    print ("Error opening image!")
    input("Press Enter to exit...")
    exit(-1);
xys = []
t_xys = []
w = len(img)
h = len(img[0,:])
for i in range(w):
    for j in range(h):
        if sum(img[i,j,:]) == 0:
            xys.append(str(i) + "\n")
            xys.append(str(j) + "\n")
        elif img[i,j,2] - img[i,j,1] > 50 and img[i,j,2] - img[i,j,0] > 50:
            t_xys.append(str(i) + "\n")
            t_xys.append(str(j) + "\n")

f = open(os.path.splitext(mapfile)[0] + '.cxy','w')
f.writelines(xys)
f.write("---TARGETS---\n");
f.writelines(t_xys)
f.close()
print ("Done!")