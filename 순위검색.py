def solution(info, query):
    answer = []

    data = dict()
    for lang in ['cpp', 'java', 'python', '-']:
        for job in ['backend', 'frontend', '-']:
            for career in ['junior', 'senior', '-']:
                for food in ['chicken', 'pizza', '-']:
                    data[lang+job+career+food] = []

    for i in info:
        lst = i.split()
        for lang in [lst[0], '-']:
            for job in [lst[1], '-']:
                for career in [lst[2], '-']:
                    for food in [lst[3], '-']:
                        data[lang+job+career+food].append(int(lst[4]))

    for key in data.keys():
        data[key].sort()

    for q in query:
        lst = q.split()
        check = data[lst[0]+lst[2]+lst[4]+lst[6]]
        score = int(lst[7])

        l = len(check)
        start, end, tmp = 0, l-1, l
        while start <= end:
            mid = (start+end)//2
            if check[mid] >= score:
                tmp = mid
                end = mid-1
            else:
                start = mid+1

        answer.append(l-tmp)

    return answer
