c = 0
for _ in range(5):
  a = int(input())
  if a < 40:
    a = 40
  c += a
print(c // 5)
