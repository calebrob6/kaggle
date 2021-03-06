#!/usr/bin/python
import cv2
import numpy as np
import time
import os
import re

startTime = time.time()

labels = []
images = []

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

DATA_DIR = "./data/"
TRAINING_DIR = "./training/"
IMAGES_DIR = "./images/"


startTime = time.time()
print "Setting up data for training"
for fname in range(7):
    label = int(fname)       
    image = cv2.imread("mean"+str(fname)+".png", cv2.IMREAD_GRAYSCALE)
    labels.append(label)
    images.append(image)
print "Finished setting up images in %s seconds" % (time.time()-startTime)
print "Starting training"
model = cv2.createLBPHFaceRecognizer(radius=2,neighbors=8)
model.setInt("recordFaces",0)
model.train(np.asarray(images),np.asarray(labels))
print "Finished training model in %s seconds" % (time.time()-startTime)

f=open("results.txt","w")
dirList=os.listdir(IMAGES_DIR)
dirList.sort(key=natural_keys)
i=1
for fname in dirList:
    image = cv2.imread(IMAGES_DIR+fname, cv2.IMREAD_GRAYSCALE)
    [pLabel, pConfidence] = model.predict(image)
    f.write(fname + " -- " + str(pLabel) + "\n")
    #print fname + " -- " + str(pLabel) + "\n"
    print str(i)+"/"+str(len(dirList)) 
    i+=1
f.close()
