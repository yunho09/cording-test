import sys
from collections import deque
stack = deque()
a = int(sys.stdin.readline())
for i in range(1, a + 1):
  stack.append(i)
while len(stack) != 1:
  stack.popleft()
  b = stack.popleft()
  stack.append(b)
print(stack[0])