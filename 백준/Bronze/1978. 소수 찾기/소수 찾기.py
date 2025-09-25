import sys
import math
a=int(input())

def prime_number(x):
    if x==1: return 0
    for i in range(2,math.floor(math.sqrt(x))+1):
        if x%i==0 and i!=x:
            return 0
    return 1

nums=list(map(int, sys.stdin.readline().split()))
result=0
for j in nums:
    result+=prime_number(j)
print(result)