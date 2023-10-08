def dfs(values, pmmd, index, n, val, dir, minVal, maxVal, visited):
    if index == n - 1:
        return minVal, maxVal

    res = 0
    if dir == 0:
        visited[0] += 1
        res = val + values[index + 1]
    elif dir == 1:
        visited[1] += 1
        res = val - values[index + 1]
    elif dir == 2:
        visited[2] += 1
        res = val * values[index + 1]
    elif dir == 3:
        visited[3] += 1
        if val < 0 <= values[index + 1]:
            res = -(abs(val) // values[index + 1])
        else: res = val // values[index + 1]

    print(index, val, res, dir)

    if index == n-2:
        minVal = min(minVal, res)
        maxVal = max(maxVal, res)

    for idx, val in enumerate(pmmd):
        if val > visited[idx]:
            minVal, maxVal = dfs(values, pmmd, index + 1, n, res, idx, minVal, maxVal, visited)

    return minVal, maxVal

n = int(input())
values = list(map(int, input().split()))
pmmd = list(map(int, input().split()))
minVal = 1e9
maxVal = -1e9

for idx, val in enumerate(pmmd):
    visited = [0] * 4
    if val > 0:
        minVal, maxVal = dfs(values, pmmd, 0, n, values[0], idx, minVal, maxVal, visited)

print(maxVal)
print(minVal)
