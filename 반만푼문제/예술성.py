n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 그룹의 개수를 관리합니다.
group_n = 0

# 각 칸에 그룹 번호를 적어줍니다.
group = [
    [0] * n
    for _ in range(n)
]
group_cnt = [0] * (n * n + 1)  # 각 그룹마다 칸의 수를 세줍니다.
visited = [
    [False] * n
    for _ in range(n)
]

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# (x, y) 위치에서 DFS를 진행합니다.
def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        # 인접한 칸 중 숫자가 동일하면서 방문한 적이 없는 칸으로만 이동이 가능합니다.
        if in_range(nx, ny) and not visited[nx][ny] and maps[nx][ny] == maps[x][y]:
            visited[nx][ny] = True
            group[nx][ny] = group_n
            group_cnt[group_n] += 1
            dfs(nx, ny)


# 그룹을 만들어줍니다.
def make_group():
    global group_n

    group_n = 0

    # visited 값을 초기화 해줍니다.
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    # DFS를 이용하여 그룹 묶는 작업을 진행합니다.
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_n += 1
                visited[i][j] = True
                group[i][j] = group_n
                group_cnt[group_n] = 1
                dfs(i, j)


def get_art_score():
    art_score = 0

    # 특정 변을 사이에 두고
    # 두 칸의 그룹이 다른 경우라면
    # (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수) x 그룹 a를 이루고 있는 숫자 값 x 그룹 b를 이루고 있는 숫자 값
    # 만큼 예술 점수가 더해집니다.
    for i in range(n):
        for j in range(n):
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if in_range(nx, ny) and maps[i][j] != maps[nx][ny]:
                    g1, g2 = group[i][j], group[nx][ny]
                    num1, num2 = maps[i][j], maps[nx][ny]
                    cnt1, cnt2 = group_cnt[g1], group_cnt[g2]

                    art_score += (cnt1 + cnt2) * num1 * num2

    # 중복 계산을 제외해줍니다.
    return art_score // 2


def get_score():
    # Step 1. 그룹을 형성합니다.
    make_group()

    # Step 2. 예술 점수를 계산해줍니다.
    return get_art_score()


#십자 회전 반시계방향
def turnPlus():
    nextMaps = [[0] * n for _ in range(n)]

    #새 공간에 회전값 넣기 nextMaps[i][j] = maps[n-1-j][i]
    for i in range(n):
        for j in range(n):
            if i == n//2 or j == n//2:
                nextMaps[i][j] = maps[j][n-1-i]
            else:
                nextMaps[i][j] = maps[i][j]


    #다시 맵에 대입
    for i in range(n):
        for j in range(n):
            maps[i][j] = nextMaps[i][j]


def subRotate(b):
    #a next, b small
    sn = len(b)
    tmp = [[0] * sn for _ in range(sn)]

    for i in range(sn):
        for j in range(sn):
            tmp[j][sn-1-i] = b[i][j]

    return tmp



#작은 정사각형 시계방향으로 회전
def turnRect():
    nextMaps = [[0] * n for i in range(n)]

    #전체 복사(십자가 남길려고)
    for i in range(n):
        for j in range(n):
            nextMaps[i][j] = maps[i][j]

    n2 = n // 2
    smallMaps = [[0] * n2 for _ in range(n2)]
    #좌상단 정사각형
    for i in range(n2):
        for j in range(n2):
            smallMaps[i][j] = maps[i][j]

    smallMaps = subRotate(smallMaps)

    for i in range(n2):
        for j in range(n2):
            nextMaps[i][j] = smallMaps[i][j]


    #우상단 정사각형
    for i in range(n2):
        for j in range(n2+1,n):
            smallMaps[i][j-n2-1] = maps[i][j]

    smallMaps = subRotate(smallMaps)

    for i in range(n2):
        for j in range(n2+1,n):
            nextMaps[i][j] = smallMaps[i][j-n2-1]


    #좌하단 정사각형
    for i in range(n2+1,n):
        for j in range(n2):
            smallMaps[i-n2-1][j] = maps[i][j]

    smallMaps = subRotate(smallMaps)

    for i in range(n2 + 1, n):
        for j in range(n2):
            nextMaps[i][j] = smallMaps[i-n2-1][j]

    #우하단 정사각형
    for i in range(n2+1,n):
        for j in range(n2+1,n):
            smallMaps[i-n2-1][j-n2-1] = maps[i][j]

    smallMaps = subRotate(smallMaps)

    for i in range(n2 + 1, n):
        for j in range(n2 + 1, n):
            nextMaps[i][j] = smallMaps[i-n2-1][j-n2-1]

    #맵 다시 지정
    for i in range(n):
        for j in range(n):
            maps[i][j] = nextMaps[i][j]


#3번의 회전 값
for i in range(4):
    ans += get_score()
    turnPlus()
    turnRect()

print(ans)

