N, M, K = map(int, input().split())
maze=[list(map(int, input().split())) for _ in range(N)]
K=K-1
answer = [0]
next=True
for i in range(N-1):
    
    for m in range(M):
        if maze[i+1][K+m]==1:
            next=False
            break

    if not next:
        break
    #들어갈 수 있다면? 
    answer.append(i+1)


for i in range(M):
    idx=answer[-1]
    maze[idx][K+i]=1

for row in maze:
    print(*row)