import math


def solution(str1, str2):
    def search(s, ref):
        for i in range(len(s) - 1):
            temp = s[i:i + 2]
            if 65 <= ord(temp[0]) <= 90 and 65 <= ord(temp[1]) <= 90:
                ref.setdefault(temp, 0)
                ref[temp] += 1

        return ref

    ref1 = search(str1.upper(), dict())
    ref2 = search(str2.upper(), dict())

    mother = 0
    son = 0
    for key in ref1.keys() | ref2.keys():
        if ref1.get(key) and ref2.get(key):
            a = ref1[key]
            b = ref2[key]
            son += min(a, b)
            mother += max(a, b)
        elif ref1.get(key):
            mother += ref1[key]
        else:
            mother += ref2[key]

    if mother == 0:
        answer = 65536
    else:
        answer = math.trunc((son / mother) * 65536)

    return answer
