n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
res = 1e9

def dfs(idx, now):
    global res

    if idx == n//2:
        a = 0
        b = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += data[i][j]
                elif not visited[i] and not visited[j]:
                    b += data[i][j]

        res = min(res, abs(a-b))
    else:
        for i in range(now, n):
            if not visited[i]:
                visited[i] = True
                dfs(idx + 1, i + 1)
                visited[i] = False



dfs(0,0)
print(res)