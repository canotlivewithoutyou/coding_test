T = int(input())

for tc in range(1, T + 1):
    code = input()
    
    inpt = input()
    
    count = {}
    
    for k in code:
        count[k]=0
    
    for i in inpt:
        if i in count:
            count[i]+=1
        else:
            continue
     
    cnt=0
    for r, c in count.items():
        if c > cnt:
            cnt = c
    
    print(f'#{tc} {cnt}')