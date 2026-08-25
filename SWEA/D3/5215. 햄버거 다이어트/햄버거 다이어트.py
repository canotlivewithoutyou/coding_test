def dfs(idx, score, calorie):
    global max_score
    
    if calorie > L:
        return
    
    if score> max_score:
        max_score=score
        
    if idx == N:
        return
    
    dfs(idx+1, score+nums[idx][0], calorie+nums[idx][1])
    
    dfs(idx+1, score, calorie)

T = int(input())

for tc in range(1, T+1):
    N, L= map(int, input().split())
    
    nums = [list(map(int, input().split())) for _ in range(N)]
    # 민기의 맛에 대한 점수(Ti)와 칼로리를 나타내는 Ki
    
    max_score=0
    dfs(0,0,0)
    
    print(f'#{tc} {max_score}')