import sys
from collections import deque
stack = deque()
a = int(sys.stdin.readline())
for _ in range(a):
  b = sys.stdin.readline().split()
  if b[0] == 'push':
    if len(b) > 1:
      stack.append(b[1])
  elif b[0] == 'pop':
    if len(stack) >= 1:
      print(stack.popleft())
    else:
      print(-1)
  elif b[0] == 'size':
    print(len(stack))
  elif b[0] == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif b[0] == 'front':
    if len(stack) >= 1:
      print(stack[0])
    else:
      print(-1)
  elif b[0] == 'back':
    if len(stack) >= 1:
      print(stack[len(stack) - 1])
    else:
      print(-1)