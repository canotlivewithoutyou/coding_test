from collections import deque

for _ in range(1, 11):
    tc = int(input())
    inpt = list(map(int, input().split()))
    
    q = deque()
    
    for num in inpt:
        q.append(num)
        
    isDone = False
    while isDone==False:
        for i in range(1, 6):
            k= q.popleft()
            if k-i > 0:
                q.append(k-i)
            else: 
                q.append(0)
                isDone=True
                break
            
    print(f'#{tc}', *q)