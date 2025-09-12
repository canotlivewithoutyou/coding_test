import sys
x=int(input())
nums=list(map(int, sys.stdin.readline().split()))
y=int(input())
result=0
for i in range(x):
    if y == nums[i]:
        result+=1
print(result)