a = [int(input()) for _ in range(5)]
sum = 0
for v in a:
  sum += int(v)
print(sum//5)
print(sorted(a)[2])
