from collections import deque

n, m = map(int, input().split()) #격자 크기, 사람의 수
maps = [[0] * (n+1) for _ in range(n+1)] #0은 빈공간 1은 베이스캠프 2는 갈수 없는 곳
for i in range(1, n+1):
    data = list(map(int, input().split()))
    for j in range(1, n+1):
        maps[i][j] = data[j-1]


mart = [(0,0)] #번호와 가고 싶은 편의점 위치
human = [(0,0) for _ in range(m+1)] #사람 위치
visited = [[0] * (n+1) for _ in range(n+1)] #베이스캠프나 편의점 체크
ans = 0 # 걸린시간
count = m #도착하지 못한 사람 수

for _ in range(m): #편의점 정보 받기
    x, y = map(int, input().split())
    mart.append((x, y))

#바로 못갈때 최단거리
def bfs(x, y, mx, my):
    # 상좌우하
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    qVisited = [[0] * (n+1) for _ in range(n+1)]
    step = [0] * 4 #방향별 거리
    isStep = [0] * 4
    qVisited[x][y] = 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 1 <= nx < n+1 and 1 <= ny < n+1:
            q = deque()
            q.append((nx,ny))

            qVisited[nx][ny] = 1
            while q:
                qx, qy = q.popleft()

                if qx == mx and qx == my:
                    isStep[d] = 1
                    break

                for qd in range(4):
                    qx2 = qx + dx[qd]
                    qy2 = qy + dx[qd]
                    if 1 <= qx2 < n + 1 and 1 <= qy2 < n + 1:
                        if maps[qx2][qy2] < 2 and not visited[qx2][qy2]:
                            visited[qx2][qy2] = 1
                            step[d] += 1
                            q.append((qx2, qy2))



    for i in range(4):
        if isStep and step[i] > 0 and max(step):
            x = x + dx[i]
            y = y + dy[i]


    return x, y

# 최단거리 구하기
def minDist(ans):
    #상좌우하
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    #해당 초에 포함된 사람들 움직임
    for i in range(1, ans):
        #더이상 사람이 없음
        if i > m:
            break
        mx, my = mart[i][0], mart[i][1]
        #사람의 좌표
        x, y = human[i][0], human[i][1] #현재 위치
        if mx == x and my == y: continue #편의점 도착했으면 다음으로
        mi, mj = x, y #최단거리 좌표
        curDist = abs(mx - mi) + abs(my - mj)#현재거리
        minDist = 1e9
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            #격자안에서 거리가 최소이면 변경
            if 1 <= nx < n+1 and 1 <= ny < n+1:
                dist = abs(mx - nx) + abs(my - ny)
                if dist < curDist and dist < minDist:
                    mi, mj = nx, ny
                    minDist = dist

        if maps[mi][mj] == 2:
            mi, mj = bfs(mi, mj, mx, my)


        human[i] = (mi, mj) #최소 거리로 이동


#편의점 도착
def depMart(ans):
    global count
    for i in range(1,ans):
        if i > m : break
        x, y = human[i][0], human[i][1]
        mx, my = mart[i][0], mart[i][1]

        #편의점 도착이라면 방문
        if mx == x and my == y and maps[x][y] != 2:
            visited[x][y] = 1
            count -= 1

# 베이스캠프 보내기
def goBase(ans):
    #예) ans = 1분에 들어오면 1번 사람
    if ans > m :
        return
    mx, my = mart[ans][0], mart[ans][1] # 1번사람이 가고싶은 마트 좌표
    mi = mj =0 #최단거리 좌표
    minDist = 1e9 #최단거리
    for i in range(1, n+1): #베이스캠프 고르기
        for j in range(1, n+1):
            if maps[i][j] == 2:
                continue
            if maps[i][j] == 1:
                #베이스캠프가 마트랑 최단거리면
                dist = abs(mx - i) + abs(my - j)
                if dist < minDist:
                    mi = i
                    mj = j
                    minDist = dist

    visited[mi][mj] = 1
    human[ans] = (mi, mj)

#마지막에 갈 수 없는 곳으로 바꾸기
def checkNotGo():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if visited[i][j] == 1:
                maps[i][j] = 2

while True:
    if count == 0:
        break
    ans += 1
    minDist(ans)#최단거리이동
    depMart(ans)#편의점도착
    goBase(ans)#베이스보내기
    checkNotGo()#visited 다 막기

print(ans)