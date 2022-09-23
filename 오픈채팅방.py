def solution(record):
    name = dict()
    for r in record:
        ipt = r.split()
        if ipt[0] != 'Leave':
            name[ipt[1]] = ipt[2]

    answer = []
    for r in record:
        ipt = r.split()
        if ipt[0] == 'Enter':
            answer.append(name[ipt[1]] + '님이 들어왔습니다.')
        elif ipt[0] == 'Leave':
            answer.append(name[ipt[1]] + '님이 나갔습니다.')

    return answer
