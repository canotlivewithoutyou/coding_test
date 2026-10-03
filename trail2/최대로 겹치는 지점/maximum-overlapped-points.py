N = int(input())

points = []

for _ in range(N):
    x1, x2 = map(int, input().split())

    points.append((x1, 1))   # 시작
    points.append((x2, -1))  # 끝


# 좌표가 같다면 시작(1)을 끝(-1)보다 먼저 처리
points.sort(key=lambda x: (x[0], -x[1]))

cnt = 0
answer = 0

for x, v in points:
    cnt += v
    answer = max(answer, cnt)

print(answer)