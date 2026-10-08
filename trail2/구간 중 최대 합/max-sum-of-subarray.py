N, K = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
for i in range(0, N-K+1):
    current=0
    for j in range(K):
        current += nums[i+j]
    result = max(result, current)

print(result)