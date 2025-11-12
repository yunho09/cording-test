import sys
from collections import deque
a, b = map(int, sys.stdin.readline().split())
list = []
stack = deque(range(1, a + 1))
while len(stack) != 1:
  for i in range(b):
    c = stack.popleft()
    stack.append(c)
  list.append(stack.pop())
print('<', end='')
for i in list:
  print(i, end=', ')
print(stack[0], end='')
print('>')