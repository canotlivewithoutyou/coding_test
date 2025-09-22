import sys

n, b = map(int, sys.stdin.readline().split())
i=1
res=''
while n!=0:
    num=(n%(b**i))//(b**(i-1))
    if num>=10:
        res+=chr(num+55)
    else:
        res+=str(num)
    n=n-num*(b**(i-1))
    i+=1
print(res[::-1])