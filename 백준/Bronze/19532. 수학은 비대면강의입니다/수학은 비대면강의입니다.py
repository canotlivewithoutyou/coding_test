import sys
a,b,c,d,e,f=map(int, sys.stdin.readline().split())

if (b*d-e*a)!=0:
    y=(c*d-f*a)//(b*d-e*a)
    x=(c*e-f*b)//(e*a-b*d)
else:
    x=(c-f)//(a-d)
    y=(c-a*x)//b
print(x,y)