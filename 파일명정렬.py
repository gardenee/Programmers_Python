def solution(files):
    answer = []
    data = dict()

    for file in files:
        head = ''
        i = 0
        while True:
            o = ord(file[i])
            if 48 <= o <= 57:
                break
            if 65 <= o <= 90 or 97 <= o <= 122:
                head += file[i].upper()
            else:
                head += file[i]
            i += 1

        num = ''
        while i < len(file):
            if ord(file[i]) < 48 or ord(file[i]) > 57:
                break
            else:
                num += file[i]
            i += 1

        if num == '':
            num = -1
        data.setdefault(head, [])
        data[head].append([num, file])

    keys = list(data.keys())
    keys.sort()
    for key in keys:
        curr = data[key]
        temp = set()

        for c in curr:
            temp.add(int(c[0]))
        temp = list(temp)
        temp.sort()

        for num in temp:
            for c in curr:
                if int(c[0]) == num:
                    answer.append(c[1])

    return answer
