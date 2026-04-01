import sys
n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
arr2 = list(map(int, sys.stdin.readline().split()))
arr1.sort()
arr2.sort(reverse=True)
res = 0
for i in range(0, n):
    res += arr1[i] * arr2[i]
print(res)