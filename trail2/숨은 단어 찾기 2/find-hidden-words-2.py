N, M = map(int, input().split())

board = [input().strip() for _ in range(N)]

dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 0, 1, -1, -1, 0, -1, 1]


def solve():
    cnt = 0
    for r in range(N):
        for c in range(M):
            isString=False

            if board[r][c]!='L':
                continue
            
            for d in range(8):
                for k in range(1, 3):
                    nr = r + dr[d]*k
                    nc = c + dc[d]*k

                    if not(0<=nr<N and 0<=nc<M) or board[nr][nc]!='E':
                        isString=False
                        break

                    isString=True

                if isString:
                    cnt+=1
    return cnt

cnt = solve()
print(cnt)