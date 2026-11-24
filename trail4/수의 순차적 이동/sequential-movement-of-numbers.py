N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

where = [None]*(N*N+1)

for r, row in enumerate(maze):
    for c, num in enumerate(row):
        where[num] = (r, c)

# 상, 하, 좌, 우, 왼쪽위, 왼쪽아래, 오른쪽위, 오른쪽아래
dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, -1, 1, 1]

for _ in range(M):
    for cnt in range(1, N*N+1):
        r, c = where[cnt]
        best = 0

        for d in range(8):

            nr = r + dr[d]
            nc = c + dc[d]

            if 0<=nr<N and 0<=nc<N and maze[nr][nc]>best:
                best = maze[nr][nc]
        
        a, b = where[best]
        maze[r][c], maze[a][b] = best, cnt
        where[cnt], where[best] = (a, b), (r, c)
    
for row in maze:
    print(*row)