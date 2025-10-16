import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
c = sys.stdin.readline().strip()
print(int(a)+int(b)-int(c))
a = a + b
print(int(a)-int(c))
