import cv2
import numpy as np

DATA_DIR = "./data/"
IMAGE_DIR = "./images/"

f = open(DATA_DIR+"test.csv","r")

header = f.readline()
i=0

for line in f:
    pixelArr = line.strip("\n").strip("\"").split(" ")
    pixelArr = [int(a) for a in pixelArr]
    cv2.imwrite(IMAGE_DIR+str(i)+".png",np.asarray(pixelArr).reshape(48,48))
    i+=1

f.close()
