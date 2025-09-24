import sys
a,b,c=map(int, sys.stdin.readline().split())
d=c-a

x=d//(a-b)
y=d%(a-b)+a #나머지 값
i=0
while y>0:
    i+=1
    y=y-a
    if y>0:
        y=y+b
print(x+i)