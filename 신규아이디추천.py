def solution(new_id):
    answer = ''
    ref = '~!@#$%^&*()=+[{]}:?,<>/'
    new_id = new_id.lower()

    for x in ref:
        new_id = new_id.replace(x, '')

    for i in new_id:
        if i == '.':
            if answer and answer[-1] == '.':
                continue
        answer += i

    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:len(answer)-1]

    if answer == '':
        answer = 'a'

    if len(answer) > 15:
        answer = answer[:15]

    while answer and answer[-1] == '.':
        answer = answer[:len(answer)-1]

    while len(answer) < 3:
        answer += answer[-1]

    return answer

