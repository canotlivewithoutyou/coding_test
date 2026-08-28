for tc in range(1, 11):
    length = int(input())
    
    inpt = input()
    
    see = {"}":"{", "]":"[", ">":"<", ")": "("}
    stack = []
    
    result =1 
    for ch in inpt:
        if ch in "{(<[":
            stack.append(ch)
        elif stack and see[ch]==stack[-1]:
            stack.pop()
        else:
            result = 0
    
    if len(stack) != 0:
        result = 0
        
    print(f'#{tc} {result}')