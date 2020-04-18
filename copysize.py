import sys, os

fpin = sys.argv[1]
fpout = sys.argv[2]
cursize = sys.argv[3]

f = open(fpout, "w", encoding="utf-8")

for line in open(fpin, encoding="utf-8"):
    print(line)
    f.write(line)
    if ((os.path.getsize(fpout) / 1024 )  > int(cursize)):
        break
f.close