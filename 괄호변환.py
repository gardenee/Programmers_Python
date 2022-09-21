import sys
sys.setrecursionlimit(10**5)


def solution(p):

    def progress(w):
        if p == '':
            return ''
        u, v = prog2(w)

        if check(u):
            if v == '':
                return u
            else:
                return u + progress(v)
        else:
            return fix(u, v)


    def prog2(w):
        cnt = 0
        u = ''
        v = ''

        for i in range(len(w)):
            if w[i] == "(":
                cnt += 1
            else:
                cnt -= 1
            if i != 0 and cnt == 0:
                u = w[:i+1]
                v = w[i+1:]
                break

        return u, v


    def check(u):
        cnt = 0

        for x in u:
            if x == "(":
                cnt += 1
            else:
                if cnt <= 0:
                    return False
                else:
                    cnt -= 1

        if cnt > 0:
            return False
        else:
            return True


    def fix(u, v):
        rtn = "(" + progress(v) + ")"

        u = u[1:-1]
        for x in u:
            if x == "(":
                rtn += ")"
            else:
                rtn += "("

        return rtn


    return progress(p)
