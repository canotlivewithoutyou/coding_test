def dfs(idx, depth):
    global result

    # 최단거리를 구하는 것이므로 가지치기
    if depth > result:
        return 

    # idx = Goal 이라면 return
    if idx == G:
        result = min(result, depth)

    # 방문 체크
    visited[idx] = True

    for next_node in node[idx]:
        # 아직 방문하지 않았다면
        if not visited[next_node]:
            dfs(next_node, depth+1)
            # 방문 체크 해제
            visited[next_node] = False


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    node = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())

        # 양방향 노드 
        node[a].append(b)
        node[b].append(a)

    S, G = map(int, input().split())

    # 방문 배열 체크 
    visited = [False]*(V+1)

    result = 10000

    dfs(S, 0)

    if result == 10000:
        result=0
        
    print(f"#{tc} {result}")