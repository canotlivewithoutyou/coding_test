for tc in range(1, 11):
    length, inpt = input().split()
    
    length=int(length)
    
    stack=[]
    
    for ch in inpt:
        if stack and ch==stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    
    print(f'#{tc} {"".join(stack)}')