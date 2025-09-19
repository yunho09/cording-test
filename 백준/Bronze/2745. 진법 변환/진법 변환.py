a, b = input().split()
b = int(b)
c = 0
for i, v in enumerate(reversed(a)):
  if '0' <= v <= '9':
    num = int(v)
  else:
    num = ord(v) - ord('A') + 10
  c += num * (b ** i)
print(c)