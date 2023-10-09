n, m, x, y, k = map(int, input().split()) # n = 세로 m = 가로 주사위(x,y) 액션갯수 k
maps = [ list(map(int, input().split())) for _ in range(n) ]
actions = list(map(int, input().split())) # 1 = 동 2 = 서 3 = 북 4 = 남
dia = [0] * 6 # 배열값 = 주사위 위치 0 = 1 , 1 = 2, 2 = 3, 3 = 4, 4 = 5, 5 = 6
step = [(2,3,1,4), (2,3,5,0), (5,0,1,4), (0,5,1,4), (2,3,0,5), (2,3,4,1)]
res = [5,4,3,2,1,0]
now = (x,y)
diaNow = 0


for i in actions:
    x, y = now[0], now[1]
    if i == 1: #동
        nx = x + 1
        ny = y
    elif i == 2: #서
        nx = x - 1
        ny = 0
    elif i == 3: #북
        nx = x
        ny = y - 1
    elif i == 4: #남
        nx = x
        ny = y + 1

    if nx < 0 and ny < 0 and nx > m and ny > n:
        continue

    now = (nx, ny)
    diaNow = step[diaNow][i - 1]

    print(now, diaNow, dia)

    if maps[ny][nx] == 0:
        maps[ny][nx] = dia[diaNow]
    else :
        dia[diaNow] = maps[ny][nx]
        maps[ny][nx] = 0

    print(dia[res[diaNow - 1] - 1])