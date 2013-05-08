#!/usr/bin/python
import cv2
import numpy as np
import time
import os

startTime = time.time()

labels = []
images = []


DATA_DIR = "./data/"
TRAINING_DIR = "./training/"


startTime = time.time()
print "Setting up data for training"
dirList=os.listdir(TRAINING_DIR)
for fname in dirList:
    label = int(fname.split("_")[0])        
    image = cv2.imread(TRAINING_DIR+fname, cv2.IMREAD_GRAYSCALE)
    labels.append(label)
    images.append(image)
print "Finished setting up images in %s seconds" % (time.time()-startTime)
print "Starting training"
model = cv2.createLBPHFaceRecognizer(radius=2,neighbors=8)
model.setInt("recordFaces",0)
model.train(np.asarray(images),np.asarray(labels))
print "Finished training model in %s seconds" % (time.time()-startTime)
