def change(n, k):
    i = 0
    while True:
        if k ** (i + 1) > n:
            break
        i += 1

    result = ""
    for j in range(i, -1, -1):
        mul = k ** j
        result += str(n // mul)
        n %= mul

    return result


def solution(n, k):
    answer = 0

    n = change(n, k)
    n = n.replace("0", " ")
    nums = list(map(int, n.split()))

    for num in nums:
        if num != 1:
            temp = 1
        else:
            temp = 0

        for i in range(2, int(round(num ** 0.5, 0)) + 1):
            if num % i == 0:
                temp = 0
                break
        answer += temp

    return answer
