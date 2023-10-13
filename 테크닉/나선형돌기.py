arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
tmp = [0] * (3 * 3)  # 일자 배열


def make1Arr(arr):
    n = len(arr)  # 배열길이
    dx = [0, 1, 0, -1]  # 좌하우상
    dy = [-1, 0, 1, 0]
    x, y = n // 2, n // 2  # 중앙값
    moveCount = 0  # 2번 방향 바뀌면 거리 1증가
    d = 0  # 방향
    dist = 1  # 반복횟수

    # 중앙도 삽입
    # tmp[0] = arr[x][y]
    # idx = 1  # tmp의 인덱스
    # 아래는 중앙은제외
    idx = 0  # tmp의 인덱스
    flag = True
    while flag :
        for _ in range(dist):  # 이동하면서 tmp에 값 넣기
            nx = x + dx[d]
            ny = y + dy[d]
            if nx == 0 and ny == -1:
                flag = False
                break
            tmp[idx] = arr[nx][ny]
            idx += 1
            x = nx
            y = ny

        moveCount += 1  # 방향 전환수
        d = (d + 1) % 4  # 방향바꾸기
        if moveCount == 2:  # 2번바꾸면 거리 1증가
            dist += 1
            moveCount = 0


make1Arr(arr)
print(tmp)