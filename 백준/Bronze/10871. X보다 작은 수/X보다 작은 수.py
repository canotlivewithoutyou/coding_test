import sys
a, b=map(int, sys.stdin.readline().split())
nums=list(map(int, sys.stdin.readline().split()))
result=[]
for i in nums:
    if i<b:
        result.append(i)
print(*result)