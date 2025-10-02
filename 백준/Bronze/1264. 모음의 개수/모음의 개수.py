import sys
d = "aeiouAEIOU"
while True:
  a = sys.stdin.readline().rstrip()
  if a == '#':
    break
  c = sum(1 for i in a if i in d)
  print(c)
  c = 0
