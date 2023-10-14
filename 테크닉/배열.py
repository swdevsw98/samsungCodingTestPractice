n = 5
maps = []
maps.append(([0] * (n+1)))
print(maps)
for i in range(n):
  maps.append([0] + list(map(int, input().split())))

print(maps)