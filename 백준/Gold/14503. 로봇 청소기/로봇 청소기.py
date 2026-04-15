import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A, B, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr[A][B] = 2
count = 1
turncount = 0

while True:
    for i in range(4):
        # 북
        if d == 0:
            d = 3
            if arr[A][B-1] == 0:
                B -= 1
                arr[A][B] = 2
                count += 1
                turncount = 0
                break
        # 동
        elif d == 1:
            d = 0
            if arr[A-1][B] == 0:
                A -= 1
                arr[A][B] = 2
                count += 1
                turncount = 0
                break
        # 남
        elif d == 2:
            d = 1
            if arr[A][B+1] == 0:
                B += 1
                arr[A][B] = 2
                count += 1
                turncount = 0
                break
        # 서
        elif d == 3:
            d = 2
            if arr[A+1][B] == 0:
                A += 1
                arr[A][B] = 2
                count += 1
                turncount = 0
                break
        turncount += 1


    # 네 방향 모두 1 or 2
    if turncount == 4:
        #북
        if d == 0:
            if arr[A+1][B] == 1:
                break
            else:
                A += 1
        #동
        elif d == 1:
            if arr[A][B-1] == 1:
                break
            else:
                B -= 1
        #남
        elif d == 2:
            if arr[A-1][B] == 1:
                break
            else:
                A -= 1
        #서
        elif d == 3:
            if arr[A][B+1] == 1:
                break
            else:
                B += 1
        turncount = 0
print(count)