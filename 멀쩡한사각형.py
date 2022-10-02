def solution(w, h):
    def gdc(a, b):
        temp = b
        b = a % b
        a = temp
        if b == 0:
            return a
        else:
            return gdc(a, b)

    n = gdc(max(w, h), min(w, h))

    return w * h - n * (w // n + h // n - 1)
