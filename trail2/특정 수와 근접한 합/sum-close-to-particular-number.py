N, S = map(int, input().split())

nums = list(map(int, input().split()))

nsum=sum(nums)
diff = float('inf')


for i in range(N):
    for j in range(i+1, N):
        T = nsum-(nums[i]+nums[j])
        diff = min(diff, abs(T-S))

print(diff)

        