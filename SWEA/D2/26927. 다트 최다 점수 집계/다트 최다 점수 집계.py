T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    dart= input()
    
    count = {}
    
    for k in dart:
        kk = int(k)
        if kk in count:
            count[kk]+=1
        else:
            count[kk]=1
    
    result, result_cnt = 0, 0
    for i, j in count.items():
        if j>result_cnt:
            result = i
            result_cnt = j
        elif j==result_cnt:
            if i>result:
                result=i
                result_cnt=j
    
    print(f'#{tc} {result} {result_cnt}')