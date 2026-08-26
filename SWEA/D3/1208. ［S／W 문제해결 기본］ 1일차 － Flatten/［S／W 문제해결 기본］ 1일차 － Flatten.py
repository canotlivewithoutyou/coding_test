for tc in range(1, 11):
    dump = int(input())
    
    nums = list(map(int, input().split()))
    
    for _ in range(dump):
        alpha = max(nums)
        beta = min(nums)
        alpha_idx = nums.index(alpha)
        beta_idx = nums.index(beta)
        
        nums[alpha_idx]-=1
        nums[beta_idx]+=1
        
    result = max(nums) - min(nums)
    
    print(f'#{tc} {result}')