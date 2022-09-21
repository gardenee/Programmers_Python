def solution(N, stages):
    dp = [0] * (N+2)
    for stage in stages:
        dp[stage] += 1

    fail = dict()
    passed = dp[-1]
    for i in range(N, 0, -1):
        passed += dp[i]
        if passed == 0:
            rate = 0
        else:
            rate = dp[i]/passed

        fail.setdefault(rate, [])
        fail[rate].append(i)

    keys = list(fail.keys())
    keys.sort(reverse=True)
    answer = []
    for key in keys:
        lst = fail[key]
        answer += lst[::-1]

    return answer
