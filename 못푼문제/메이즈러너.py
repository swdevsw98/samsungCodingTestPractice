#n = 미로 크기 m = 참가자 수 k = 게임시간
n, m ,k = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]
# -10은 출구
# -9 ~ -1은 벽이다
# 0 은 사람이다
# 1이상은 사람의 수이다

#참가자
person = [list(map(int, input().split())) for _ in range(m)]
ex_x, ey_y = map(int, input().split())

for i in range(n):
    for j in range(n):
        if maps[i][j] == 0:
            continue
        maps[i][j] *= -1

for x,y in person:
    maps[x-1][y-1] += 1

maps[ex_x-1][ey_y-1] = -10

# 이동 거리 합
distSum = 0
# 출구좌표
ex = (ex_x, ey_y)
#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def findEx():
    global ex
    for i in range(n):
        for j in range(n):
            if maps[i][j] == -10:
                ex = (i, j)


# 사람을 움직이는 함수
def moveAll():
    global ex, distSum
    newMaps = [[0] * n for _ in range(n)]
    findEx()
    ex, ey = ex[0], ex[1]
    # 상하좌우 순서
    # 현재칸 보다 출구까지 거리가 최단거리
    for i in range(n):
        for j in range(n):
            if maps[i][j] < 0:
                newMaps[i][j] = maps[i][j]
                continue
            if maps[i][j] == 0:
                continue

            curDist = abs(ex - i) + abs(ey - j)
            minDist = curDist
            minI = i
            minJ = j

            #(i,j)에 사람이 있을 때
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]

                if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] >= 0:
                    dist = abs(ex - nx) + abs(ex - ny)

                    if dist < minDist:
                        minDist = dist
                        minI = nx
                        minJ = ny

            # 움직일 수 없는 상황(벽)이면 가만히 있기
            if minDist == curDist:
                continue

            distSum += 1

            if maps[minI][minJ] == -10:
                continue

            newMaps[minI][minJ] += maps[i][j]

    for i in range(n):
        for j in range(n):
            maps[i][j] = newMaps[i][j]






# 작은 정사각형 회전
#(x,y) d는 거리
def subRotate(x, y, d):
    global n
    tmp = [[0] * n for _ in range(n)]
    tmp2 = [[0] * n for _ in range(n)]

    for i in range(x, x+d):
        for j in range(y, y+d):
            #0,0부터 시작하게 넣기
            tmp[i-x][j-y] = maps[i][j]

    n2 = d + 1
    for i in range(n2):
        for j in range(n2):
            if -9 <= tmp[i][j] <= -1:
                tmp[i][j] += 1

            tmp2[j][n2+1-i] = tmp[i][j]
    # 회전하면 내구도 1감소

    for i in range(x,x+d):
        for j in range(y, y+d):
            maps[i][j] = tmp2[i-x][j-y]

# 미로가 회전
def rotate():
    global ex
    findEx()
    minDist = 100000
    # 1. 가장작은 정사각형 잡기
    for i in range(n):
        for j in range(n):
            if maps[i][j] <= 0 :
                continue
            dist = max(abs(i-ex[0]), abs(j-ex[1]))
            minDist = min(minDist, dist)

    bestI, bestJ = 0, 0
    # 2. 좌상단 좌표
    for i in range(n-minDist):
        for j in range(n-minDist):

            flagExit, flagPerson = False, False
            for r in range(i, i+minDist):
                for c in range(j, j+minDist):
                    if maps[r][c] == -10: flagExit = True
                    if maps[r][c] > 0 : flagPerson = True

            if flagPerson and flagExit:
                bestI = i
                bestJ = j
        if bestI != 0: break

    # 2. 시계방향 90도로 회전
    subRotate(bestI, bestJ, minDist)

def isFinish():
    for i in range(n):
        for j in range(n):
            if maps[i][j] > 0:
                return False

findEx()
for i in range(1, k):
    # 사람 움직이기
    moveAll()

    # 모든 참가자가 탈출하면 종료
    if isFinish():
        break


    # 미로 회전하기
    rotate()

findEx()
print(distSum)
print(ex[0], ex[1])