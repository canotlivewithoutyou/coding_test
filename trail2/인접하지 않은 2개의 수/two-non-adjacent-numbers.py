N = int(input())

nums = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i+2, N):
        result = max(result, nums[i]+nums[j])

print(result)