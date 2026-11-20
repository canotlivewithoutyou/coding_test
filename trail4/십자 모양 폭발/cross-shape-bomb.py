N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())

# 위치 정보를 idx로 맞추기
r, c = r-1, c-1

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

k = maze[r][c]

for d in range(4):
    for i in range(1, k):
        nr = r + dr[d]*i
        nc = c + dc[d]*i

        if 0<=nr<N and 0<=nc<N:
            maze[nr][nc] = 0

maze[r][c] = 0

# -------------------------------------------
for j in range(N):
    idx = N-1 
    for i in range(N-1, -1, -1):
        if maze[i][j] != 0:
            maze[idx][j] = maze[i][j]

            if idx != i:
                maze[i][j] = 0

            idx -= 1

for row in maze:
    print(*row)