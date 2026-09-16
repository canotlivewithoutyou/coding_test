def dfs(idx):
    global answer

    if idx == (N+1):
        answer+=1
        return 
    
    for c in range(1, K+1): # c: color
        possible = True

        for next_node in graph[idx]:

            if color[next_node]==c:
                possible=False
                break

        if possible:
            color[idx]=c
            dfs(idx+1)
            color[idx]=0

T= int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    color = [0]*(N+1)
    answer=0

    dfs(1)

    print(f'#{tc} {answer}')