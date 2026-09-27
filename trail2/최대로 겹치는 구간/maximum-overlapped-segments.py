N = int(input())

event = {}

for _ in range(N):
    x1, x2 = map(int, input().split())

    # 시작점에서는 선분이 하나 추가
    event[x1] = event.get(x1, 0) + 1

    # 끝점에서는 선분이 하나 빠짐
    event[x2] = event.get(x2, 0) - 1


current = 0
answer = 0

# 좌표가 작은 곳부터 확인
for x in sorted(event):
    current += event[x]
    answer = max(answer, current)

print(answer)