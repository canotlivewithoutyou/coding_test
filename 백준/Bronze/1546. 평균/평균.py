import sys
k=int(input())
nums=list(map(int, sys.stdin.readline().split()))
max_num=max(nums)
result=0
for i in range(k):
    nums[i]=nums[i]/max_num*100
    result+=nums[i]
print(result/k)