import sys
list = []
for i in range(8):
  a = int(sys.stdin.readline())
  b = (i + 1, a)
  list.append(b)
list.sort(key=lambda x:x[1], reverse=True)
c = 0
d = []
for i in list[:5]:
  c = c + i[1]
  d.append(i[0])
print(c)
d.sort()
for i in d:
  print(i, end=' ')
