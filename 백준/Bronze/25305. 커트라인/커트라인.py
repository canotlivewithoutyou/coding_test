import sys
N,k=map(int, input().split())
nums=list(map(int, sys.stdin.readline().split()))

nums.sort(reverse=True)
print(nums[k-1])