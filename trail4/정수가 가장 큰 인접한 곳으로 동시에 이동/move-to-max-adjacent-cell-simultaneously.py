N, M, T = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ori_location = []

for _ in range(M):
    r, c = map(int, input().split())
    ori_location.append((r-1, c-1))

# 움직일 다음 위치 찾기 
def move(r,c):
    best = 0
    a, b = r, c
    for d in range(4):

        nr = r + dr[d]
        nc = c + dc[d]

        if 0<=nr<N and 0<=nc<N and maze[nr][nc]>best:
            best = maze[nr][nc]
            a, b = nr, nc 

    return a, b

for _ in range(T):

    # 일단 살아있는 구슬을 전부 움직이고
    move_location = []
    for r, c in ori_location:
        move_location.append(move(r, c))

    # 혼자 도착한 구슬만 다음 턴으로 넘겨서 
    ori_location = []
    for row in move_location:
        if move_location.count(row)==1:
            ori_location.append(row)
    
print(len(ori_location))