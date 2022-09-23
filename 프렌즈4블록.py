def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])

    dy = [0, 1, 0, 1]
    dx = [0, 0, 1, 1]

    while True:
        temp = set()
        for i in range(m - 1):
            for j in range(n - 1):
                curr = board[i][j]
                if curr == ' ':
                    continue
                if curr == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    for k in range(4):
                        temp.add(tuple([i + dy[k], j + dx[k]]))

        if not temp:
            break
        answer += len(temp)

        for t in temp:
            board[t[0]][t[1]] = ' '

        for j in range(n):
            for i in range(m - 1, 0, -1):
                if board[i][j] == ' ':
                    for d in range(1, i + 1):
                        if board[i - d][j] != ' ':
                            board[i][j] = board[i - d][j]
                            board[i - d][j] = ' '
                            break

    return answer
