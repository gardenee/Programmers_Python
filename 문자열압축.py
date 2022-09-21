def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2+1):
        result = ""
        prev = s[:i]
        j = i
        cnt = 1
        while j+i-1 < len(s):
            curr = s[j:j+i]
            if prev == curr:
                cnt += 1
            else:
                if cnt == 1:
                    result += prev
                else:
                    result += str(cnt) + prev
                cnt = 1
                prev = curr
            j += i

        if cnt == 1:
            result += curr
        else:
            result += str(cnt) + prev

        if j < len(s):
            result += s[j:]
        answer = min(answer, len(result))

    return answer
