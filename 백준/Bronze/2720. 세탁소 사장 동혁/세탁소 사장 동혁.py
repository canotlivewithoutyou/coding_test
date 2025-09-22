import sys

a=int(input())
for _ in range(a):
    res=[0,0,0,0]
    num=int(input())
    while num!=0:
        if num>=25:
            num=num-25
            res[0]+=1
        elif num>=10:
            num=num-10
            res[1]+=1
        elif num>=5:
            num=num-5
            res[2]+=1
        else:
            res[3]=num
            num=0
    print(*res)