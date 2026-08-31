from collections import deque

T= int(input())

for tc in range(1, T+1):
    M = int(input())
    inpt = list(map(int, input().split()))
    
    queue = deque()
    number = 1
    result = []
    
    for k in inpt:
        if k == 1:
            queue.append(number)
            number+=1
        
        elif k == 2:
            result.append(queue.popleft())
    
    print(f'#{tc}', *result)