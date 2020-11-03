# python 13
# understanding the mysteries of the len function

a = ["hello","i", "am", "doing", "code"]

print len(a)
print len(a[1])

for i in range(len(a)):
  if len(a[i]) > 3:
     print i, a[i]
