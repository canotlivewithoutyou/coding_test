def solution(k, num):
    cnt=0
    while num%k == 0:
        num= num//k
        cnt+=1
    
    return cnt
        
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    result=[]
    k_nums=[2, 3, 5, 7, 11]
    
    for i in k_nums:
        result.append(solution(i, N))
    
    print(f'#{tc}', *result)