N = int(input())

answer = []
visit = [False]*(N+1)

def solution():

    if len(answer)==N:
        print(*answer)
        return

    for i in range(1, N+1):

        if visit[i]:
            continue
        
        answer.append(i)
        visit[i] = True

        solution()

        answer.pop()
        visit[i] = False

solution()