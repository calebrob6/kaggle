#!/usr/bin/python
import cv2
import numpy as np
import time

startTime = time.time()

DATA_DIR = "./data/"
TRAINING_DIR = "./training/"

f = open(DATA_DIR+"train.csv","r")

header = f.readline()

labels = []
images = []

i=0
for line in f:
    if i%1000 == 0:
        print "Read %s images" % i
    data = line.split(",")
    labels.append(data[0])

    imageTemp = np.asarray([int(a) for a in data[1].strip("\n").strip("\"").split(" ")]).reshape(48,48)
    images.append(imageTemp)
    i+=1
f.close()

print "Finished reading file information in %s seconds\n" % (time.time()-startTime)

for l in range(len(labels)):
    cv2.imwrite(TRAINING_DIR+str(labels[l])+"_"+str(l)+".png", images[l])

print "Finished writing training information\n"
print "Time taken: %s\n" % (time.time()-startTime)
