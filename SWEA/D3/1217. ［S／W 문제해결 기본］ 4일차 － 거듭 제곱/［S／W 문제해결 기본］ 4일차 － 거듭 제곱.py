for _ in range(1, 11):
    tc = int(input())
    N, M = map(int, input().split())
    result=1
    for _ in range(M):
        result=result*N
            
    print(f'#{tc} {result}')