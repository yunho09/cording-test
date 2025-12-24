import sys
n, s = map(int, sys.stdin.readline().split())
slist = list(map(int, sys.stdin.readline().split()))
result = 0
def dfs(index, currentsum, count):
    global result
    if index == len(slist):
        if count > 0 and currentsum == s:
            result += 1
        return
    dfs(index + 1, currentsum + slist[index], count+1)
    dfs(index + 1, currentsum, count)
dfs(0, 0, 0)
print(result)