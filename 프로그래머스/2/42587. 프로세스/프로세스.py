from collections import deque
def solution(priorities, location):
    ABC = deque()
    for i in range(len(priorities)):
        ABC.append(i)

    queue = deque()
    for i in priorities:
        queue.append(i)

    res = []
    while queue:
        a = queue.popleft()
        b = ABC.popleft()
        if any(a < x for x in queue):
            queue.append(a)
            ABC.append(b)
        else:
            res.append(b)
            if b == location:
                return len(res)
                break

