T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    
    nums.sort()
    
    nums_sum=0
    for i in range(1, len(nums)-1):
        nums_sum+=nums[i]
    result = nums_sum / (len(nums)-2)
    
    print(f'#{tc} {int(round(result, 0))}')