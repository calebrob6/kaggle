#!/usr/bin/python
import cv2
import numpy as np
import time
import os

startTime = time.time()
meanCount = dict()

means = []
for a in range(7):
    meanCount[a] = 0
    mean = []
    for i in range(48):
        t = []
        for j in range(48):
            t.append(0)
        mean.append(t)
    means.append(mean)


DATA_DIR = "./data/"
TRAINING_DIR = "./training/"


startTime = time.time()
print "Summing pixels"
dirList=os.listdir(TRAINING_DIR)
for fname in dirList:
    label = int(fname.split("_")[0])
        
    image = cv2.imread(TRAINING_DIR+fname)

    iC=0
    for i in image:
        jC=0
        for j in i:
            means[label][iC][jC]+=j[0]
            jC+=1
        iC+=1
    meanCount[label]+=1
print "Finished summing pixels in %s seconds\n" % (time.time()-startTime)

startTime = time.time()
print "Calculating means and writing images"
for a in range(7):
    for i in range(48):
        for j in range(48):
            means[a][i][j]=round(means[a][i][j]/meanCount[a])
    cv2.imwrite("mean"+str(a)+".png",np.asarray(means[a]))
print "Finished in %s seconds\n" % (time.time()-startTime)

