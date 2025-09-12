import sys
a,b=map(int, sys.stdin.readline().split())
nums=[x for x in range(1,a+1)]
k,q=0,0
while k!=b:
    i,j=map(int, sys.stdin.readline().split())
    nums[i-1:j]=nums[i-1:j][::-1]
    k+=1
print(*nums)