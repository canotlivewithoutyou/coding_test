from collections import deque

def bfs(r, c):
    q = deque()
    q.append((r, c, 0))

    visited[r][c] == True

    while q:
        r, c, cnt = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0<=nr<N and 0<=nc<N:
                #벽도 아니고 방문한적도 없다면
                if maze[nr][nc]!= '1' and not visited[nr][nc]:

                    if maze[nr][nc]=='3':
                        return cnt

                    visited[nr][nc]=True
                    q.append((nr, nc, cnt+1))
    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    maze = [input() for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    sr, sc = 0, 0

    for r in range(N):
        for c in range(N):
            if maze[r][c]=='2':
                sr, sc = r, c

    visited = [[False]*N for _ in range(N)]

    answer = bfs(sr, sc)

    print(f'#{tc} {answer}')