import sys
a = sys.stdin.read().strip()
lis = [0] *  27
for i in a:
  if 'a' <= i <= 'z':
    b = ord(i) - ord('a')
    lis[int(b)] += 1
for index, i in enumerate(lis):
  if i == max(lis):
    c = index + ord('a')
    print(chr(c), end='')
