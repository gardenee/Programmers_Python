def solution(fees, records):
    result = dict()

    for r in records:
        ipt = r.split()
        result.setdefault(ipt[1], [])
        result[ipt[1]].append(ipt[0])

    numbers = list(result.keys())
    numbers.sort()

    answer = [0] * len(numbers)

    for n in range(len(numbers)):
        curr = result[numbers[n]]
        if len(curr) % 2 == 1:
            curr.append("23:59")

        time = 0
        for i in range(len(curr) // 2):
            _in = curr[2 * i]
            _out = curr[2 * i + 1]
            time += int(_out[:2]) * 60 + int(_out[3:]) - int(_in[:2]) * 60 - int(_in[3:])

        answer[n] += fees[1]
        if time > fees[0]:
            answer[n] += (time - fees[0]) // fees[2] * fees[3]
            if (time - fees[0]) % fees[2] != 0:
                answer[n] += fees[3]

    return answer
