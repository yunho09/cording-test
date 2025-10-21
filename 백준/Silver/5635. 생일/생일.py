import sys
n = int(sys.stdin.readline())
lis = []
for i in range(n):
  a = sys.stdin.readline().split()
  lis.append(a) 
lis.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(lis[len(lis)-1][0])
print(lis[0][0])
