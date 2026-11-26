N, M, K = map(int, input().split())
scores = list(map(int, input().split()))

location = [1]*K
answer = 0

def solution(turn, score):
    global answer
    
    # N번의 턴을 모두 사용했다면 최댓값 갱신
    if turn == N:
        answer = max(answer, score)
        return 

    for k in range(K):
        before = location[k]
        after = min(M, before+scores[turn])
        location[k] = after
        
        gained = 1 if before < M and after == M else 0

        solution(turn + 1, score+gained)

        location[k] = before

solution(0,0)
print(answer)
