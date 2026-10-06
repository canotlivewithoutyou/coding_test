N = int(input())

spot = [list(map(int, input().split())) for _ in range(N)]

answer = float('inf')
for i in range(1, N-1):
    dist = 0
    prev_idx = 0

    for j in range(1, N):
        if i==j:
            continue

        dist += abs(spot[prev_idx][0]-spot[j][0]) + abs(spot[prev_idx][1]-spot[j][1])
        prev_idx = j

    answer = min(answer, dist)

print(answer)