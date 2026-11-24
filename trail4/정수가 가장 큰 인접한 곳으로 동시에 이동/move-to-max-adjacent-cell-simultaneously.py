from collections import Counter

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

    # 각 좌표에 구슬이 몇 개 도착?
    arrivals = Counter(move(r, c) for r, c in ori_location)
    
    # 구슬이 딱 1개 도착한 좌표만 다음 턴으로 넘기기
    ori_location = [pos for pos, cnt in arrivals.items() if cnt==1]
    
print(len(ori_location))