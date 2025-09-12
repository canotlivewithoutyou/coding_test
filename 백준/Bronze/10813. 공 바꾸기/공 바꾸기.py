import sys
x,y=map(int, sys.stdin.readline().split())
q, p=0,0
nums=[i for i in range(1,x+1)]
while q!=y:
    num1, num2 = map(int, sys.stdin.readline().split())
    p,nums[num2-1]=nums[num2-1],nums[num1-1]
    nums[num1-1]=p
    q+=1
print(*nums)