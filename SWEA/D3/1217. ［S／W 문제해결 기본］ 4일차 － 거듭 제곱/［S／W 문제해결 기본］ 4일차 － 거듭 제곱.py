def solution(a, cnt):
    global result
    
    if cnt == b:
        return result
    
    result = result*a
    
    return solution(a, cnt+1)

for _ in range(10):
    tc = int(input())
    
    a, b = map(int, input().split())
    
    result = 1
    solution(a, 0)
    print(f'#{tc} {result}')