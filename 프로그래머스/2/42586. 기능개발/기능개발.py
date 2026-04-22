def solution(progresses, speeds):
    time = []
    res = []
    for i in range(len(progresses)):
        a = progresses[i]
        count = 0
        while a < 100:
            a += speeds[i]
            count += 1
        time.append(count)

    cur = time[0]
    count = 1
    for i in range(1, len(time)):
        if time[i] <= cur:
            count += 1
        else:
            res.append(count)
            count = 1
            cur = time[i]
    res.append(count)
    return res