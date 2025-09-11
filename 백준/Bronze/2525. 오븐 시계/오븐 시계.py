a,b=map(int,input().split())
c=int(input())
k=0
if c>=60:    #60분 이상이라면
    k=c//60     #시간이랑
    c = c%60    #분으로 나누고
    if a+k>=24:     
       a=a+k-24
    else:
        a=a+k
if b+c>=60:
    b=(b+c)-60
    if a+1==24:
        a=0
    else:
        a=a+1
else:
    b=b+c
print(a, b)