from collections import deque

N, L, R = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False for _ in range(N)] for _ in range(N)]


def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N


def bfs(x, y):
    q = deque()
    coords = []
    total = 0
    q.append([x, y])
    coords.append([x, y])
    total += board[x][y]
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_valid(nx, ny) and (not visited[nx][ny]) and L <= abs(board[x][y] - board[nx][ny]) <= R:
                visited[nx][ny] = True
                coords.append([nx, ny])
                total += board[nx][ny]
                q.append([nx, ny])
    for coord in coords:
        board[coord[0]][coord[1]] = total // len(coords)
    if len(coords) > 1:
        return True
    return False


ans = 0
while True:
    cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
                cnt += 1
    if cnt == N * N:
        print(ans)
        break
    ans += 1
