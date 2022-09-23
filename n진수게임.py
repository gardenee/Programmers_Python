def solution(n, t, m, p):
    def change(num, n):
        if num == 0:
            rtn = '0'
        else:
            rtn = ''

        while num != 0:
            temp = num % n
            if temp >= 10:
                temp = chr(temp + 55)
            rtn += str(temp)
            num //= n

        return rtn[::-1]

    number = ''
    i = 0
    while True:
        number += change(i, n)
        i += 1
        if len(number) >= t * m:
            break

    number = number[p - 1:]
    answer = number[::m]
    answer = answer[:t]

    return answer
