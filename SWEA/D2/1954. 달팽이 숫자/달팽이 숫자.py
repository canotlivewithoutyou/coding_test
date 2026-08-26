T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    result = [[0]*N for _ in range(N)]
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    r, c, d, cnt = 0, 0, 0, 1
    
    for _ in range(N*N):
        result[r][c] = cnt
        
        nr = r + dr[d]
        nc = c+ dc[d]
        
        if 0<=nr<N and 0<=nc<N and result[nr][nc]==0:
            r, c = nr, nc
        else:
            d = (d+1)%4
            r = r + dr[d]
            c = c + dc[d]
            
        cnt +=1
        
    print(f'#{tc}')
    for row in result:
        print(' '.join(map(str, row)))