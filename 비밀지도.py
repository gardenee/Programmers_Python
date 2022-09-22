def solution(n, arr1, arr2):
    answer = [[' '] * n for _ in range(n)]

    def check(arr, answer):
        for i in range(n):
            line = arr[i]
            num = bin(line)[2:].zfill(n)
            for j in range(n):
                if num[j] == '1' and answer[i][j] == ' ':
                    answer[i][j] = '#'
        return answer

    answer = check(arr1, answer)
    answer = check(arr2, answer)

    for i in range(n):
        temp = ''
        for j in range(n):
            temp += answer[i][j]
        answer[i] = temp

    return answer
