answer = [0] * 11
score = 0

def dfs(n, info, curr, x):
    global answer
    global score

    if n == 0:
        ryan = 0
        apeach = 0
        for i in range(11):
            if curr[i] == info[i] == 0:
                continue
            elif curr[i] > info[i]:
                ryan += 10-i
            else:
                apeach += 10-i

        if (ryan-apeach) >= score:
            if (ryan-apeach) > score:
                answer = curr
            else:
                for i in range(10, -1, -1):
                    if curr[i] < answer[i]:
                        break
                    if curr[i] > answer[i]:
                        answer = curr
                        break
            score = ryan - apeach

        return

    for i in range(x, 11):
        temp = curr.copy()
        if info[i] < n:
            temp[i] = info[i] + 1

        if i == 10 and n > 0:
            temp[i] += n

        if temp != curr:
            dfs(n - temp[i], info, temp, x+1)


def solution(n, info):
    global answer

    dfs(n, info, [0] * 11, 0)

    if score == 0:
        answer = [-1]

    print(answer)
    return answer
