#!/usr/bin/python
import sys

if len(sys.argv)!=3:
    print "Usage: ./convertResults.py <input.txt> <output.csv>\n"
    sys.exit(0)

inFile = sys.argv[1]
outFile = sys.argv[2]
f = open(outFile,"w")
for i in open(inFile,"r"):
    a = i.split("--")
    f.write(a[1].strip()+"\n")
f.close()
