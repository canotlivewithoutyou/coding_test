N= 19

board = [list(map(int, input().split())) for _ in range(N)]

# 오른쪽, 아래, 오른쪽 아래, 왼쪽 아래, 
dr = [0, 1, 1, 1]
dc = [1, 0, 1, -1]

win, core_r, core_c = 0, 0, 0

for r in range(N):
    for c in range(N):

        if board[r][c]==0:
            continue
        

        current = board[r][c]

        for d in range(4):
            cnt = 0

            for k in range(5):

                nr = r + dr[d]*k
                nc = c + dc[d]*k

                if not (0<=nr<N and 0<=nc<N):
                    break

                if board[nr][nc]!=current:
                    break

                cnt+=1

            if cnt == 5:
                win = current 

                core_r = r + dr[d]*2
                core_c = c + dc[d]*2

                break

        if win != 0:
            break
    if win!=0:
        break

print(win)

if win!=0:
    print(core_r+1, core_c+1)
