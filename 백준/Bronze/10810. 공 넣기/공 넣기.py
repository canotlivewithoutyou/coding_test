import sys
a,b=map(int, sys.stdin.readline().split())
nums=[0]*(a+1)
q=0
while q!=b:
    i,j,k=map(int,sys.stdin.readline().split())
    for y in range(i,j+1):
        nums[y]=k
    q+=1
print(*nums[1:])