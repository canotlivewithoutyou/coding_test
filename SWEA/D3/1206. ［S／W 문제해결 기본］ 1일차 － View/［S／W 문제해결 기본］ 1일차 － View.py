for tc in range(1, 11):
    N = int(input())
    
    nums = list(map(int, input().split()))
    
    # 앞뒤로 인덱스 2번째칸까지 보는데
    # max값으로 보면 되고
    # 그 max값을 빼는 방향으로 구현해보면 되지 않을까... 
    result = 0
    for k in range(2, len(nums)-2):
        line = max(nums[k-2], nums[k-1], nums[k+1], nums[k+2])
        answer = nums[k] - line
        if answer > 0:
            result += answer
        
    print(f'#{tc} {result}')