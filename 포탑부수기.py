from collections import deque

n, m, k = map(int,input().split()) #(1,1) - (n,m) 격자 k = 시뮬 횟수
maxK = k
maps = []#0 = 부서짐, 양수 = 포탑 공격력
maps.append([0] * (m+1))
for _ in range(n):
    maps.append([0] + list(map(int,input().split())))
time = [[k] * (m+1) for _ in range(n+1)] #언제 쐈는지 체크
isAttack = [[0] * (m+1) for _ in range(n+1)]#포탑에 맞았는지

best = 0 #가장 강한 포탑의 공격력
attacker = (0 ,0) #공격자
king = (0,0) #공격대상
damage = n + m


# 공격자 선정
def step1():
    global attacker, k
    arr = [] #낮은 포탑이 여러개일때 넣을 배열
    #공격력이 가장 낮은 포탑 선택
    count = 0 # 낮은 포탑의 갯수 새기
    mi = mj = 0 #낮은 포탑의 좌표
    minAtt = 5010
    for i in range(1, n+1): #낮은 공격력 찾기
        for j in range(1, m+1):
            if maps[i][j] < minAtt and maps[i][j] != 0:
                minAtt = maps[i][j]
                mi = i
                mj = j

    for i in range(1, n+1): #낮은 공격력을 가진 포탑이 몇개인지 찾기
        for j in range(1, m+1):
            if maps[i][j] == minAtt:
                arr.append((i,j))
                count += 1

    if count == 1: #낮은공격력이 한명이라면
            attacker = (mi, mj)
            time[mi][mj] -= 1

    else:
        last = maxK #횟수
        lCount = 0
        for x, y in arr: #
            if time[x][y] == last:#최근에 공격했는가?
                lCount += 1
            if time[x][y] < last:#더 최근에 공격한 포탑이 있다면
                lCount = 1
                last = time[x][y]
                mi = x
                mj = y

        if lCount == 1: #최근 공격이 하나
            attacker = (mi, mj)
            time[mi][mj] -= 1

        else: #최근 공격이 둘이상
            sumrc = 0
            arr = sorted(arr, key = lambda x:x[1], reverse=True)
            for x, y in arr:
                if x + y > sumrc:  # 최근에 공격하고 i + j 가 큰값, j가 큰 값
                    sumrc = x + y
                    mi = x
                    mj = y

            attacker = (mi, mj)
            time[mi][mj] -= 1



#최단경로 구하기
def bfs(att, king):
    #레이저
    dx = [0, 1, 0, -1] #우하좌상
    dy = [1, 0, -1, 0]

    rVisited = [[0] * (m+1) for _ in range(n+1)] #레이저 경로
    q = deque()
    x,y = att[0], att[1] #공격자
    kx, ky = king[0], king[1] #목표지
    rVisited[kx][ky] = 1
    q.append((kx,ky))

    while q:
        qx, qy = q.popleft()

        for d in range(4):
            nx = qx + dx[d]
            ny = qy + dy[d]

            if 1<=nx<n+1 and 1<=ny<m+1:
                if maps[nx][ny] != 0 and rVisited[nx][ny] == 0: #방문한적없고 맵이 부서지지 않은 곳 방문
                    rVisited[nx][ny] = rVisited[qx][qy] + 1
                    q.append((nx,ny))

    minDist = 1000
    minD = -1
    #최단경로 있는지 확인
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 1 <= nx < n+1 and 1<= ny < m+1:
            if minDist > rVisited[nx][ny] and rVisited[nx][ny]:
                minDist = rVisited[nx][ny]
                minD = d


    if minD == -1: #포탄 공격
        dx = [-1, -1, 0, 1, 1, 1, 0, -1] #상 상좌 좌 좌하 하 우하 우 우상
        dy = [0, -1, -1, -1, 0, 1, 1, 1]
        isAttack[kx][ky] = 1
        for d in range(8):
            nx = kx + dx[d]
            ny = ky + dy[d]

            if nx < 1: nx += n
            elif nx > n: nx = nx % n

            if ny < 1: ny += m
            elif ny > m: ny = ny % m

            if maps[nx][ny] != 0:
                isAttack[nx][ny] = 1

    else: #그 방향으로 공격
        q = deque()
        nx = x + dx[minD]
        ny = y + dy[minD]
        isAttack[nx][ny] = 1
        q.append((nx,ny))
        dist = minDist

        while q: #공격
            qx, qy = q.popleft()

            for d in range(4):
                dxs, dys = qx + dx[d], qy + dy[d]

                if 1<= dxs < n+1 and 1 <= dys < m+1: #격자안에서
                    if rVisited[dxs][dys] == dist - 1 and maps[dxs][dys] != 0: #경로따라가기
                        dist -= 1
                        q.append((dxs, dys))
                        isAttack[dxs][dys] = 1

    isAttacked()

#포탑 공격력 낮추기
def isAttacked():
    for i in range(1, n+1):
        for j in range(1,m+1):
            if isAttack[i][j]:
                if i == attacker[0] and j == attacker[1]: continue
                if i == king[0] and j == king[1]: #공격자리면 데미지
                    maps[i][j] -= maps[attacker[0]][attacker[1]] + damage
                    if maps[i][j] < 0 :
                        maps[i][j] = 0
                else:#주변자리
                    maps[i][j] -= (maps[attacker[0]][attacker[1]] + damage) // 2
                    if maps[i][j] < 0 :
                        maps[i][j] = 0

#공격
def step2():
    #king = 가장 강한 포탑
    global king
    arr = [] #공격력이 같은 좌표
    best = 0 #최대 공격력
    count = 0 #공격력이 같은 포탑수
    for i in range(1, n+1):# 공격력 대장 찾기
        for j in range(1, m+1):
            if i == attacker[0] and j == attacker[1]: continue
            if maps[i][j] > best: #공격력이 높은 포탑
                best = maps[i][j]

    for i in range(1, n+1): # 가장 높은 공격력 찾기
        for j in range(1, m+1):
            if i == attacker[0] and j == attacker[1]: continue
            if maps[i][j] == best:
                count += 1
                arr.append((i,j))

    if count == 1:
        x, y = arr.pop()
        king = (x,y)

    else:
        old = 0 #오래된 포탑
        oCount = 1 #오래된 포탑 수
        ox = oy = 0

        for x, y in arr:
            if time[x][y] == old: #오래된 포탑이 두개다
                oCount += 1
            if time[x][y] > old:  # 새로운 오래된 포탑을 찾음
                old = time[x][y]
                ox = x
                oy = y
                oCount = 1


        if oCount == 1:
            king = (ox,oy)

        else:
            sumrc = 100
            arr = sorted(arr, key=lambda x: x[1])
            for x, y in arr:
                if x + y < sumrc:  # 최근에 공격하고 i + j 가 큰값, j가 큰 값
                    sumrc = x + y
                    ox = x
                    oy = y

            king = (ox,oy)


    #레이저 or 포탑 공격
    bfs(attacker, king)




#정비
def step3():
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == attacker[0] and j == attacker[1]: continue
            if not isAttack[i][j] and maps[i][j] != 0:
                maps[i][j] += 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            isAttack[i][j] = 0



# 종료 조건 = 부서지지 않은 포탑
def isFinish():
    count = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if maps[i][j] > 0:
                count += 1

    if count == 1:
        return True
    else:
        return False


while k:
    k -= 1
    step1()
    step2()
    if isFinish():
        maps[attacker[0]][attacker[1]] += damage
        break
    step3()
    maps[attacker[0]][attacker[1]] += damage


#공격력이 가장 강한 포탑 출력
for i in range(1, n+1):
    for j in range(1, m+1):
        if best < maps[i][j]:
            best = maps[i][j]

print(best)