def solution(numbers):
    a = []
    for i in numbers:
        a.append(str(i))
    result = ''.join(sorted(a, key=lambda x: x*3, reverse=True))
    return "0" if result[0] == "0" else result