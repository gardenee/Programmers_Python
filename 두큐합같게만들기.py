def solution(queue1, queue2):
    answer = 0
    q1 = queue1.copy()
    q2 = queue2.copy()
    sum1 = sum(q1)
    sum2 = sum(q2)
    N = len(q1) + len(q2) + 2
    i = 0
    j = 0
    while True:
        if answer > N:
            answer = -1
            break
        if sum1 == sum2:
            break

        answer += 1
        if sum1 > sum2:
            move = q1[i]
            q2.append(move)
            i += 1
            sum1 -= move
            sum2 += move
        else:
            move = q2[j]
            j += 1
            q1.append(move)
            sum1 += move
            sum2 -= move

    return answer
