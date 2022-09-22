def solution(dartResult):
    result = [0]
    curr = ''
    for s in dartResult:
        if s == 'S':
            result.append(int(curr))
            curr = ''
        elif s == 'D':
            result.append(int(curr) ** 2)
            curr = ''
        elif s == 'T':
            result.append(int(curr) ** 3)
            curr = ''
        elif s == '*':
            result[-1] *= 2
            result[-2] *= 2
        elif s == '#':
            result[-1] *= -1
        else:
            curr += s

    return sum(result)
