def solution(msg):
    answer = []
    ref = dict()
    for i in range(26):
        ref[chr(65 + i)] = i + 1

    n = 27
    curr = ''
    for m in msg:
        if curr == '':
            curr = m
            continue

        if ref.get(curr + m):
            curr += m
        else:
            answer.append(ref[curr])
            ref[curr + m] = n
            n += 1
            curr = m

    answer.append(ref[curr])

    return answer
