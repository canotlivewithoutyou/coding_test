T = int(input())

for tc in range(1, T+1):
    inpt = input()
    
    stack = []
    
    for k in inpt:
        stack.append(k)
        
        if len(stack) > 1 and stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()
            
    print(f'#{tc} {len(stack)}')