import sys
x=int(input())
nums=list(map(int, sys.stdin.readline().split()))
nums.sort()
print(nums[0], nums[x-1])