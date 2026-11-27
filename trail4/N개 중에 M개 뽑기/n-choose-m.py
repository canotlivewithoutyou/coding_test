N , M = map(int, input().split())

answer = []

def solution(start):

    if len(answer) == M:
        print(*answer)
        return

    for i in range(start, N+1):
        answer.append(i)
        solution(i+1)
        answer.pop()

solution(1)