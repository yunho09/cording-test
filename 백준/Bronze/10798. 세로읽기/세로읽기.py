a = [input().rstrip() for _ in range(5)]
maxlen = max(len(v) for v in a)
for b in range(maxlen):
  for c in range(5):
    if b < len(a[c]):
      print(a[c][b], end="")