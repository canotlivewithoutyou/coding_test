N, r, c = map(int, input().split())
maze= [list(map(int, input().split())) for _ in range(N)]
r, c= r-1, c-1
# 상, 하, 좌, 우 
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

print(maze[r][c], end=' ')

while True:
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0<=nr<N and 0<=nc<N and maze[r][c]<maze[nr][nc]:
            r, c = nr, nc
            next = True
            print(maze[nr][nc], end=' ')
            break

    if not next:
        break
    
    next = False
        