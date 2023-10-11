n, m = map(int, input().split())
x, y, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]  # 북동남서
dy = [0, 1, 0, -1]


def turn():
    global d
    if d == 0:
        d = 3
    elif d == 1:
        d = 0
    elif d == 2:
        d = 1
    elif d == 3:
        d = 2


count = 0

while True:
    if count == 4:
        count = 0
        # 뒤로가기
        x = x - dx[d]
        y = y - dy[d]
        if maps[x][y] == 1:
            break


    else:
        visited[x][y] = 1
        turn()
        count += 1
        nx = x + dx[d]
        ny = y + dy[d]

        # 턴한 곳이 방문한 곳이거나 인도
        if visited[nx][ny] == 1 or maps[nx][ny] == 1:
            continue

        # 다음꺼 들어가기
        count = 0
        visited[nx][ny] = 1
        x, y = nx, ny

res = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            res += 1
print(res)


