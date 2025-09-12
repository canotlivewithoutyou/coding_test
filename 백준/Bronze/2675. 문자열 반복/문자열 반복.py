import sys
k=int(input())
i=0
result=''
while i<k:
    a,b=sys.stdin.readline().split()
    b_line=list(b.rstrip('\n'))
    for j in range(0,len(b_line)):
        result+=b_line[j]*int(a)
    print(result)
    result=''
    i+=1