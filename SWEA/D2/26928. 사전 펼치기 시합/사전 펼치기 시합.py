def solution(l, r, goal, cnt):
    c = (l+r)//2
    cnt+=1
    if c==goal:
        return cnt
    elif c<goal:
        return solution(c, r, goal, cnt)
    else:
        return solution(l, c, goal, cnt)
    

T = int(input())

for tc in range(1, T+1):
    # 지우는 A, 한솔이는 B
    # c = (l + r) / 2
    
    P, Pa, Pb = map(int, input().split())
    
    a_result = solution(1, P, Pa, 0)
    b_result = solution(1, P, Pb, 0)
    
    result=''
    if a_result==b_result:
        result+='0'
    elif a_result<b_result:
        result+='A'
    else:
        result+='B'
        
    print(f'#{tc} {result}')