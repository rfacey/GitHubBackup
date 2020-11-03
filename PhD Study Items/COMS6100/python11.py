# python 11
lines = []
f = open("161.txt","r")
for l in f:
  lines.append(l.strip())
f.close()

for l in lines:
  v = l.split("re")
  if len(v) > 1:
    print "--"
    print l
    print v
    print "len = ", len(v)
    print v[1]
