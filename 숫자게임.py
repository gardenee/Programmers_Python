import heapq

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()

    for a in A:
        if not B:
            break
        b = heapq.heappop(B)
        while B and b <= a:
            b = heapq.heappop(B)
        if b > a:
            answer += 1

    return answer
