N = int(input())

nums = list(map(int, input().split()))

nnums = sorted(nums)
max_result = nnums[-1]+nnums[-2]

result=0
for i in range(N):
    for j in range(N):
        if abs(i-j)>=2:
            current = nums[i]+nums[j]
            result= max(result, current)
    
    if result == max_result:
        break

print(result)