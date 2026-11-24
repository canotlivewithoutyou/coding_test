K, N = map(int, input().split())
answer = []

def solution(cnt):

    if cnt == N:
        print(*answer)
        return 

    for i in range(1, K+1):
        answer.append(i)
        solution(cnt+1)
        answer.pop()

solution(0)