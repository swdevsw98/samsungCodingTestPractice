grid = [list(map(int,input())) for _ in range(4)]

k = int(input())
rotate_dir = [0 for _ in range(4)]
ans = 0
def flip(direction):
    if direction == 1:
        return -1
    else:
        return 1
def shift(num, direction):
    if direction == 1:
        temp = grid[num][7]
        for i in range(7,0, -1):
            grid[num][i]=grid[num][i-1]
        grid[num][0] = temp
    else:
        temp = grid[num][0]
        for i in range(7):
            grid[num][i] = grid[num][i+1]
        grid[num][7] = temp

def simulate(num, direction):
    global rotate_dir

    rotate_dir = [0 for _ in range(4)]
    rotate_dir[num] = direction
    for i in range(num-1,-1,-1):
        if grid[i][2] != grid[i+1][6]:
            rotate_dir[i] = flip(rotate_dir[i+1])
        else:
            break
    for i in range(num + 1, 4, 1):
        if grid[i][6] != grid[i-1][2]:
            rotate_dir[i] = flip(rotate_dir[i-1])
        else:
            break
    for i in range(4):
        if rotate_dir[i] != 0:
            shift(i, rotate_dir[i])




for _ in range(k):
    n,d = map(int,input().split())
    n = n-1
    simulate(n,d)

for i in range(4):

    if grid[i][0] == 1:
        ans += 2**i
print(ans)