from collections import deque
n, k = tuple(map(int, input().split()))

durability = list(map(int, input().split()))


moving_work = deque(durability)
person = deque([0 for i in range(2 * n)])


cnt = 0

def simulate():
    global cnt

    # 무빙워크 이동
    moving_work.appendleft(moving_work.pop())
    person.appendleft(person.pop())

    # n번칸 사람 내리기
    if person[n - 1]:
        person[n - 1] = 0

    # 사람 이동
    for i in range(n - 1, 0, -1):
        # 현재 위치에 사람이 없고 내구도는 남아 있으면서 이전 위치에 사람이 있는 경우
        if person[i] == 0 and person[i - 1] and moving_work[i]:
            person[i] = 1
            person[i - 1] = 0

            moving_work[i] -= 1

            if moving_work[i] == 0:
                cnt += 1
    # n번칸 사람 내리기
    if person[n - 1]:
        person[n - 1] = 0

    # 사람 올리기
    if moving_work[0]:
        moving_work[0] -= 1
        person[0] = 1

        if moving_work[0] == 0:
            cnt += 1

answer = 0
while True:
    simulate()
    answer += 1

    if cnt >= k:
        break

print(answer)