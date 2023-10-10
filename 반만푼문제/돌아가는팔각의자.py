# c[0]은 1번째 테이블 사람
c = [list(map(int, input())) for _ in range(4)]  # 0 = 12시방향 , 2 = 3시 방향, 4 = 6시 방향, 6 = 9시 방향
k = int(input())
visited = [0] * 4
res = 0


def turn(d, n):
    tmp = [0] * 8
    if d == 1:
        for i in range(8):
            if i + 1 > 7:
                tmp[(i + 1) % 8] = c[n][i]
            else:
                tmp[i + 1] = c[n][i]
    elif d == -1:
        for i in range(8):
            if i - 1 < 0:
                tmp[i + 7] = c[n][i]
            else:
                tmp[i - 1] = c[n][i]

    for i in range(8):
        c[n][i] = tmp[i]


def dfs(d, n):
    # print(d, n, visited)
    visited[n] += 1
    if n - 1 >= 0 and c[n - 1][2] != c[n][6] and not visited[n - 1]:
        # print("n-1")
        visited[n - 1] += 1
        dfs(-d, n - 1)
        turn(-d, n - 1)

    elif n + 1 <= 3 and c[n + 1][6] != c[n][2] and not visited[n + 1]:
        # print("n+1")
        visited[n + 1] += 1
        dfs(-d, n + 1)
        turn(-d, n + 1)

    if visited[n] == 1:
        turn(d, n)


for i in range(k):
    n, d = map(int, input().split())
    dfs(d, n - 1)
    for i in range(4):
        visited[i] = 0
    # print(c)

res = 1 * c[0][0] + 2 * c[1][0] + 4 * c[2][0] + 8 * c[3][0]
print(res)