n = int(input())
data = [list(map(int, input().split())) for _ in range(n * n)]
maps = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]


# 상하좌우에서 좋아하는 사람수와 빈칸 수 출력
def checkCount(x, y, idx):
    blank = 0
    love = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] == 0:
                blank += 1
                continue
            for l in range(1, 5):
                if maps[nx][ny] == data[idx][l]:
                    love += 1
                    break

    return blank, love


for i in range(n * n):
    count = [[0] * n for _ in range(n)]
    blankMax = -1
    loveMax = -1
    for j in range(n):
        for k in range(n):
            # 조건
            # map에 값이 있으면 건너뛰기
            if maps[j][k] != 0:
                count[j][k] = (0, 0)
                continue
            # j,k 맵에 i를 넣을때 갯수
            blank, love = checkCount(j, k, i)
            blankMax = max(blankMax, blank)
            loveMax = max(loveMax, love)
            count[j][k] = (blank, love)

    # 좋아요 max면 푸쉬
    arr = []
    for j in range(n):
        for k in range(n):
            tmp = count[j][k]
            if tmp[1] == loveMax and loveMax != 0:
                arr.append((j, k))

    # 빈칸 체크
    if len(arr) < 1:
        for j in range(n):
            for k in range(n):
                tmp = count[j][k]
                if tmp[0] == blankMax and blankMax != 0:
                    arr.append((j, k))

    # 행 체크
    if len(arr) > 1:
        minX = n + 1
        for idx, val in enumerate(arr):
            x = val[0]
            y = val[1]
            minX = min(minX, x)
            if minX != x:
                arr.pop(idx)

    # 열체크
    if len(arr) > 1:
        minY = n + 1
        for idx, val in enumerate(arr):
            x = val[0]
            y = val[1]
            minY = min(minY, y)
            if minY != y:
                arr.pop(idx)

    x, y = -1, -1
    if len(arr) == 0:
        for j in range(n):
            for k in range(n):
                if maps[j][k] == 0:
                    x = j
                    y = k
                    break
    else:
        x, y = arr.pop()
    maps[x][y] = data[i][0]

# 점수 계산
sum = 0
for i in range(n):
    for j in range(n):
        for k in range(n * n):
            if maps[i][j] == data[k][0]:
                blank, love = checkCount(i, j, k)
                if love == 0:
                    sum += 0
                elif love == 1:
                    sum += 1
                elif love == 2:
                    sum += 10
                elif love == 3:
                    sum += 100
                elif love == 4:
                    sum += 1000

print(sum)


