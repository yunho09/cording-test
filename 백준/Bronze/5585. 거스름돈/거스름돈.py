import sys
n = int(sys.stdin.readline())
count = 0
money = 1000
money = money - n
while money > 0:
    if money >= 500:
        money -= 500
        count += 1
    elif money >= 100:
        money -= 100
        count += 1
    elif money >= 50:
        money -= 50
        count += 1
    elif money >= 10:
        money -= 10
        count += 1
    elif money >= 5:
        money -= 5
        count += 1
    elif money >= 1:
        money -= 1
        count += 1
print(count)