T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    nums = list(map(int, input().split()))
    
    action = []
    for i in range(0, N-M+1):
        nums_sum = 0
        for j in range(M):
            nums_sum += nums[i+j]
        action.append(nums_sum)
    
    result = max(action) - min(action)
    
    print(f'#{tc} {result}')