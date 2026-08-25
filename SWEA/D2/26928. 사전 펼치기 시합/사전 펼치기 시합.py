def solution(l, r, goal):
    cnt=0
    c=0
    while c!=goal:
        c=(l+r)//2
        cnt+=1
        if goal==c:
            return cnt
        elif goal>c:
            l=c
        else:
            r=c
            

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    
    a_result=solution(1, P, Pa)
    b_result=solution(1, P, Pb)
    
    answer = ''
    if a_result == b_result:
        answer += '0'
    elif a_result<b_result:
        answer+='A'
    else:
        answer+='B'
        
    print(f'#{tc} {answer}')