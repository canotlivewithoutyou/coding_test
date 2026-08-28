def solution(a,b):
    if b==0:
        return 1
    
    return a*solution(a, b-1)

for _ in range(10):
    tc = int(input())
    
    a, b = map(int, input().split())
    
    result = solution(a,b)
    
    print(f'#{tc} {result}')