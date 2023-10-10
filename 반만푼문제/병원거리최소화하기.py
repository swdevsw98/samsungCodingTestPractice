import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
board = list()
for _ in range(N):
    board.append(list(map(int, input().split())))

hospital_coords = []
people_coords = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            people_coords.append([i, j])
        elif board[i][j] == 2:
            hospital_coords.append([i, j])


def dist(a, b, x, y):
    return abs(a - x) + abs(b - y)


def calculate_distance(hospital_coords):
    res = 0
    for people_coord in people_coords:
        temp = N * 2
        for coord in hospital_coords:
            temp = min(temp, dist(coord[0], coord[1], people_coord[0], people_coord[1]))
        res += temp
    return res


def get_min_distance():
    ans = float('inf')
    for hospital_combination in combinations(hospital_coords, M):
        ans = min(ans, calculate_distance(hospital_combination))
    return ans


if __name__ == "__main__":
    print(get_min_distance())