import sys
import heapq
heap = []
a = int(sys.stdin.readline())
for i in range(a):
  b = int(sys.stdin.readline())          
  if b == 0:
    if len(heap) > 0:
      print(-heapq.heappop(heap))
    else:
      print(0)
  elif b != 0:
    heapq.heappush(heap, -b)