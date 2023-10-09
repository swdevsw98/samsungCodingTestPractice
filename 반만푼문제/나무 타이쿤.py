n, m = map(int, input().split())

trees = [list(map(int, input().split())) for _ in range(n)]
moves = [tuple(map(int, input().split())) for _ in range(m)]

#     → ↗  ↑  ↖  ← ↙ ↓ ↘
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

sur_r = [-1, -1, 1, 1]
sur_c = [-1, 1, -1, 1]


def moved(x):
    if x < 0:
        x = x + n
    elif x >= n:
        x = x % n
    return x


nutri = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

for move in moves:
    d_idx, leng = move[0] - 1, move[1]

    for i in range(len(nutri)):
        nutri[i][0] = moved(nutri[i][0] + dr[d_idx] * leng)
        nutri[i][1] = moved(nutri[i][1] + dc[d_idx] * leng)

    for i in range(len(nutri)):
        trees[nutri[i][0]][nutri[i][1]] += 1

    for n_r, n_c in nutri:
        surround = 0
        for i in range(4):
            r = n_r + sur_r[i]
            c = n_c + sur_c[i]
            if 0 <= r < n and 0 <= c < n and trees[r][c] >= 1:
                surround += 1
        trees[n_r][n_c] += surround

    new_nutri = []
    for i in range(n):
        for j in range(n):
            if [i, j] not in nutri and trees[i][j] >= 2:
                trees[i][j] -= 2
                new_nutri.append([i, j])

    nutri = new_nutri

answer = 0
for row in trees:
    answer += sum(row)

print(answer)