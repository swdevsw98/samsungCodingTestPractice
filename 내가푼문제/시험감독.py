n = int(input())
student = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0

for a in student:
    a -= b
    if a < 0:
        cnt += 1
        continue
    if a % c == 0: cnt += (a//c) + 1
    else : cnt += (a // c) + 2


print(cnt)
