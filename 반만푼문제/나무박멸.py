#n = 격자 크기, m = 박멸이 진행된 년수 , k = 제초제 확산 범위 , c = 제초제 지속 년수
n, m, k, c = map(int,input().split())
#나무 정보
# 1~100 나무의 수 , 0은 빈칸, -1은 벽, -2는 제초제
maps = [list(map(int,input().split())) for _ in range(n)]
#살충제 년도
killMaps = [[0] * n for _ in range(n)]

#박멸한 나무의 수
ans = 0

def inRange(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

#상하좌우에서 나무가 있는 만큼 성장
def growTree():
    #상하좌우
    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]

    #1.인접한 네칸 중에 나무의 수 만큼 성장
    for i in range(n):
        for j in range(n):
            #나무가 없으면 성장 안함
            if maps[i][j] < 1 :
                continue
            #주변 나무 갯수
            nearTree = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                #주변이 나무면
                if inRange(nx,ny) and maps[nx][ny] > 0:
                    nearTree += 1

            maps[i][j] += nearTree



#상하좌우 중에 빈칸에 나무 퍼뜨리기
def spreadTree():
    #빈칸
    blank = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 0:
                blank[i][j] = 1

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #1. 벽, 다른나무, 제초제 모두 없는칸
    for i in range(n):
        for j in range(n):
            if blank[i][j] or maps[i][j] == -1:
                continue
            tree = maps[i][j]
            count = 0
            da = [0] * 4
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if inRange(nx,ny) and blank[nx][ny] and killMaps[nx][ny] <= 0:
                    da[d] = 1
                    count += 1

            if count == 0:
                continue

            #퍼트릴 나무 수
            srTree = tree // count



            for d in range(4):
                if da[d] == 0:
                    continue
                nx = i + dx[d]
                ny = j + dy[d]
                if inRange(nx, ny):
                    maps[nx][ny] += srTree


#제초제 뿌릴 곳 선택
def choiceKill():
    global ans
    #죽인 나무 수
    killTree = [[0] * n for _ in range(n)]

    #좌상, 우상, 좌하, 우하 구현
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    for i in range(n):
        for j in range(n):
            if maps[i][j] == -1:
                continue
            if maps[i][j] == 0:
                continue
            killTree[i][j] = maps[i][j]
            for d in range(4):
                for t in range(1,k+1):
                    nx = i + dx[d] * t
                    ny = j + dy[d] * t

                    if not inRange(nx,ny):
                        break

                    if maps[nx][ny] <= 0 : break
                    else:
                        killTree[i][j] += maps[nx][ny]

    maxI, maxJ = 0, 0
    sumKill = killTree[0][0]
    #제초제 뿌릴 곳 찾기
    for i in range(n):
        for j in range(n):
            if killTree[i][j] > sumKill:
                maxI = i
                maxJ = j
                sumKill = killTree[i][j]

    if maps[maxI][maxJ] == -1:
        return

    maps[maxI][maxJ] = -2
    killMaps[maxI][maxJ] = c
    ans += sumKill
    #제초제 뿌리기
    for d in range(4):
        for t in range(1,k+1):
            nx = maxI + dx[d] * t
            ny = maxJ + dy[d] * t


            if inRange(nx, ny):
                if maps[nx][ny] == -1: break
                if maps[nx][ny] == 0:
                    maps[nx][ny] = -2
                    killMaps[nx][ny] = c
                    break
                maps[nx][ny] = -2
                killMaps[nx][ny] = c

def clearKill():
    for i in range(n):
        for j in range(n):
            if killMaps[i][j] > 0:
                killMaps[i][j] -= 1




for i in range(m):
    growTree()
    spreadTree()
    clearKill()
    choiceKill()

print(ans)

