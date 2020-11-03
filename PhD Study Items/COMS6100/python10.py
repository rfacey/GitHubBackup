# python 10
words = []
lines = []
f = open("161.txt","r")
for l in f:
  lines.append(l.strip().split())
f.close()

wordlist = []
for l in lines:
  for w in l: 
    wordlist.append(w)

wordlist.sort()
for w in wordlist:
  print w
