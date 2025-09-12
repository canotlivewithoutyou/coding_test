import sys
nums=list(map(int, sys.stdin.readline().split()))
original=[1,1,2,2,2,8]
result=[]
for i in range(len(nums)):
    if nums[i]!=original[i]:
        result.append(original[i]-nums[i])
    else:
        result.append(0)
print(*result)