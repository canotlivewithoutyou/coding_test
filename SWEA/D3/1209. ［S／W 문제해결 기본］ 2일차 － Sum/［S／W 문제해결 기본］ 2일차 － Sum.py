for tc in range(1, 11):
    N=int(input())
    nums = [list(map(int, input().split())) for _ in range(100)]

    sum1, sum2, row_sum, col_sum = 0, 0, 0, 0
    
    for i in range(100): # 오른쪽 대각선
        sum1 += nums[i][i]
    
    for j in range(99, -1, -1): # 왼쪽 대각선 
        sum2 += nums[j][99-j]
    
    for row in nums: # 열 최대 
        answer = sum(row)
        if answer>row_sum:
            row_sum = answer
    
    #전치행렬 사용(열 -> 행)
    T_nums = [list(col) for col in zip(*nums)] # 행 최대 
    for row in T_nums:
        answer=sum(row)
        if answer>col_sum:
            col_sum = answer 
            
    print(f'#{tc}', max(sum1, sum2, row_sum, col_sum))