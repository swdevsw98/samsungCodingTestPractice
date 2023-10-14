from collections import deque

n = int(input()) #격자의 크기
m = int(input()) #연결지을 간선의 개수
visited = [[0] * (n+1) for _ in range(n+1)] #노드가 있는 곳
ans = 0 #감염시킨 맵 갯수
check = [0] * (n+1) #한번확인한건 체크 안함

for _ in range(m):
    i, j = map(int,input().split())
    visited[i][j] = 1
    visited[j][i] = 1

q = deque()
q.append(1)

while q:

    i = q.popleft()

    for j in range(1,n+1):
        if visited[i][j] and not check[j]:
            ans += 1
            visited[i][j] = 0
            visited[j][i] = 0
            check[j] = 1
            q.append(j)

print(ans) # 컴퓨터 수에 1은 제외