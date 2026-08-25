T = int(input())

for tc in range(1, T+1):
    tc_num = int(input())
    
    nums = list(map(int, input().split()))
    
    count = {}
    
    for k in nums:
        if k in count:
            count[k]+=1
        else:
            count[k]=1
            
    result, result_cnt = 0, 0
    
    for score, cnt in count.items():
        if cnt > result_cnt:
            result = score
            result_cnt = cnt
        elif cnt == result_cnt:
            if score>result:
                result = score
                result_cnt = cnt
        else:
            continue
    
    print(f'#{tc} {result}')