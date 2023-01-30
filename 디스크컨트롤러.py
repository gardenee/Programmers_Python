import heapq


def solution(jobs):
    N = len(jobs)
    answer = 0
    start, now = -1, 0
    heap = []

    jobs.sort()

    while N:
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        if heap:
            curr = heapq.heappop(heap)
            start = now
            now += curr[0]
            answer += now - curr[1]
            N -= 1
        else:
            now += 1

    return answer // len(jobs)