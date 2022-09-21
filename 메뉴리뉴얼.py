lst = []
menu = ""


def solution(orders, course):
    global lst
    global menu
    temp = [dict() for _ in range(len(course))]

    def dfs(n, course):
        global lst
        global menu

        if n == 0:
            lst.append(course)
            return

        for m in menu:
            if not course or ord(m) > ord(course[-1]):
                dfs(n-1, course+m)

    for order in orders:
        for c in course:
            if c <= len(order):
                lst = []
                menu = order
                dfs(c, "")

                for l in lst:
                    temp[course.index(c)].setdefault(l, 0)
                    temp[course.index(c)][l] += 1

    answer = []

    for c in course:
        key = list(temp[course.index(c)].keys())
        key.sort()

        t = []
        n = 2
        for k in key:
            if temp[course.index(c)][k] >= n:
                if temp[course.index(c)][k] > n:
                    t = []
                    n = temp[course.index(c)][k]
                t.append(k)

        answer += t

    answer.sort()

    return answer
