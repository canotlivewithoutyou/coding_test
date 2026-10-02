R, C = map(int, input().split())

board = [input().split() for _ in range(R)]

answer = 0

for r1 in range(1, R - 1):
    for c1 in range(1, C - 1):

        # 출발점과 첫 번째 점프 위치의 색 비교
        if board[r1][c1] == board[0][0]:
            continue

        for r2 in range(r1 + 1, R - 1):
            for c2 in range(c1 + 1, C - 1):

                # 두 번째 점프 위치와 도착점의 색 비교
                if board[r2][c2] == board[R - 1][C - 1]:
                    continue

                # 첫 번째와 두 번째 점프 위치의 색 비교
                if board[r1][c1] == board[r2][c2]:
                    continue

                answer += 1

print(answer)