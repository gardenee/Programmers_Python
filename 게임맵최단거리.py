def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def bfs(stack, visited, cnt):
        if not stack: return -1
        flag = False
        temp = []

        while stack:
            location = stack.pop()
            x, y = location[0], location[1]
            if visited[x][y]: continue
            if x == n - 1 and y == m - 1:
                flag = True
                break

            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                    temp.append([nx, ny])

        if not flag:
            return bfs(temp, visited, cnt + 1)
        else:
            return cnt + 1

    return bfs([[0, 0]], [[False] * m for _ in range(n)], 0)
