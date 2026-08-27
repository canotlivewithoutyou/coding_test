T = int(input())

for tc in range(1, T+1):
    inpt = input()
    result = []
    answer=1
    for k in inpt:
        if k == '{' or k=="(":
            result.append(k)
        elif (k == "}" or k == ")") and len(result)!=0 :
            p = result.pop()
            if (k == "}" and p == "{") or (k == ")" and p=="("):
                continue
            else:
                answer = 0
                break
        elif (k == "}" or k == ")") and len(result)==0 :
            answer=0
            break
    
    if len(result)!=0:
        answer = 0
        
    print(f'#{tc} {answer}')