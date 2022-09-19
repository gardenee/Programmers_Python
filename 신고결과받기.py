def solution(id_list, report, k):
    N = len(id_list)
    answer = [0] * N
    check = dict()

    for r in report:
        a, b = r.split()
        check.setdefault(b, set())
        check[b].add(id_list.index(a))

    for id in id_list:
        if check.get(id) and len(check[id]) >= k:
            for i in check[id]:
                answer[i] += 1

    return answer
