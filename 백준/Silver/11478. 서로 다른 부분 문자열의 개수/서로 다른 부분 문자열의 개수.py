import sys
input = sys.stdin.readline
S = str(input().strip())
set = set()
for i in range(1, len(S) + 1):
    for j in range(i - i, len(S) - i + 1):
        set.add(S[j : j + i])
print(len(set))