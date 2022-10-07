def solution(N, road, K):
    answer = 0
    time = [10000 * 500000] * (N + 1)
    time[1] = 0

    graph = dict()
    for r in road:
        graph.setdefault(r[0], [])
        graph.setdefault(r[1], [])
        graph[r[0]].append([r[1], r[2]])
        graph[r[1]].append([r[0], r[2]])

    check = [1]
    while check:
        curr = check.pop()
        for lst in graph[curr]:
            node, t = lst[0], lst[1]
            if time[curr] + t < time[node]:
                if node not in check: check.append(node)
                time[node] = time[curr] + t

    for t in time:
        if t <= K: answer += 1

    return answer
