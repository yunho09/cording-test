def solution(citations):
    arr = sorted(citations, reverse=True)
    
    for i in range(len(arr)):
        if arr[i] < i + 1:
            return i
    return len(arr)