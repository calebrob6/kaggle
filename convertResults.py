f = open("submission2.csv","w")
for i in open("results.txt","r"):
    a = i.split("--")
    f.write(a[1].strip()+"\n")
f.close()
