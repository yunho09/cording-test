import sys
input = sys.stdin.readline
N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))
dic = { }
for i in Nlist:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i in Mlist:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")