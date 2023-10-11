n, k = map(int, input().split())
belt = list(map(int, input().split()))  # 안전성
moving = [(i, 0) for i in range(n)]  # (벨트번호, 사람 여부))



# 시계방향 회전
def move():
    for i in range(n-1,0,-1):
        tmp = moving[i-1][0]
        tmp2 = moving[i-1][1]
        moving[i] = (tmp, tmp2)

    tmp = moving[1][0]
    tmp2 = 0
    if tmp - 1 < 0: tmp = tmp - 1 + 2 * n
    else : tmp -= 1

    moving[0] = (tmp,tmp2)

# 사람 전진
def humanMove():
    vistied = [0] * n
    for i in range(n - 1):
        # 안정성 0 이상 다음 번호에 사람있는지
        if belt[moving[i + 1][0]] > 0 and moving[i + 1][1] == 0 and moving[i][1] == 1 and not vistied[i]:
            tmp = moving[i][0]
            moving[i] = (tmp, 0)
            tmp = moving[i + 1][0]
            moving[i + 1] = (tmp, 1)
            vistied[i+1] = 1
            belt[tmp] -= 1


count = 0
flag = True
while flag:
    count += 1
    move()
    if moving[n - 1][1] == 1:
        tmp = moving[n - 1][0]
        moving[n - 1] = (tmp, 0)
    humanMove()
    if moving[n - 1][1] == 1:
        tmp = moving[n - 1][0]
        moving[n - 1] = (tmp, 0)
    if moving[0][1] == 0 and belt[moving[0][0]] > 0:
        tmp = moving[0][0]
        belt[tmp] -= 1
        moving[0] = (tmp, 1)

    br = 0
    for i in belt:
        if i == 0:
            br += 1

    if br >= k:
        flag = False

print(count)
