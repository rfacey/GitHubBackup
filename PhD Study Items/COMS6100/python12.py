# python 12
import math

n = 20
f = open("mydata.txt","w")
for i in range(n):
  xx = float(i)/float(n) * 2.0 * math.pi
  yy = math.sin(xx)
  s = str(xx) + ", " + str(yy) + "\n"
  f.write(s)
f.close()

