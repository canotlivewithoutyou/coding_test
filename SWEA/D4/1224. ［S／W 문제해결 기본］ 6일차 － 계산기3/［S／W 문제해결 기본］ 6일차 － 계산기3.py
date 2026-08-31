for tc in range(1, 11):
    
    length = int(input())
    inpt = input()
    
    priority = {'+': 1, '*': 2}
    
    stack = []
    result= []
    
    for ch in inpt:
        if ch.isdigit():
            result.append(ch)
            
        elif ch == "(":
            stack.append(ch)
            
        elif ch==")":
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        
        else:
            # *이거나 +
            while stack and stack[-1]!='(' and priority[stack[-1]]>=priority[ch]:
                result.append(stack.pop())
            
            stack.append(ch)
    
    while stack:
        result.append(stack.pop())

    # 후위표기식 계산
    calc_stack=[]
    
    for ch in result:
        if ch.isdigit():
            calc_stack.append(int(ch))
        
        else:
            b = calc_stack.pop()
            a = calc_stack.pop()
            
            if ch == "+":
                calc_stack.append(a+b)
            elif ch == "*":
                calc_stack.append(a*b)
    
    print(f'#{tc} {calc_stack[0]}')