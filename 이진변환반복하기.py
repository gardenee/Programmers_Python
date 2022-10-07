def solution(s):
    answer = [0, 0]

    def change(s, arr):
        arr[0] += 1
        tmp = len(s)
        s = s.replace('0', '')
        arr[1] += tmp - len(s)

        l = len(s)
        n = bin(l)[2:]
        if n != '1':
            return change(n, arr)
        else:
            return arr

    answer = change(s, answer)

    return answer
