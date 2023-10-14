from collections import deque

n, m = map(int, input().split()) #(1,1) - (N, M) 격
maps = [] # 0은 못지나감 1은 지나감
maps.append([0] * (m+1))
for _ in range(n):
    maps.append([0] + list(map(int,input())))
visited = [[0] * (m+1) for _ in range(n+1)]

q = deque()
q.append((1,1))
visited[1][1] = 1

dx = [-1, 1, 0, 0]#상하 좌우
dy = [0, 0, -1, 1]
while q:
    x,y = q.popleft()

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 1<= nx < n+1 and 1<= ny < m+1:
            if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))

print(visited[n][m])