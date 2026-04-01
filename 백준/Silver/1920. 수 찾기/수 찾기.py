import sys
n1 = int(sys.stdin.readline())
m1 = set(map(int, sys.stdin.readline().split()))
n2 = int(sys.stdin.readline())
m2 = list(map(int, sys.stdin.readline().split()))

for i in range(0, n2):
    if m2[i] in m1:
        print(1)
    else:
        print(0)