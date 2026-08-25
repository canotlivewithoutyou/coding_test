T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    nums = list(map(int, input().split()))
    
    count = [0]*101
    
    result = [] # 정리 점수를 기록할 리스트
    
    for k in range(N-1, -1, -1): # 거꾸로 돌아, 딕서너리에서...
        score = 0
        idx = nums[k]
        
        count[idx]+=1
        
        if idx==0:
            result.append(0)
        else:
            for q in range(idx):
                score += count[q]
            result.append(score)
    
    print(f'#{tc} {max(result)}')