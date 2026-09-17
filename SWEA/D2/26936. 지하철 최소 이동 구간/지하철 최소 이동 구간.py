from collections import deque

def bfs(start):
    q = deque()

    q.append(start)

    visited[start]=True
    distance[start]=0

    while q:
        current = q.popleft()

        if current==G:
            return distance[current]

        for next_node in node[current]:
            if not visited[next_node]:
                visited[next_node] = True
                distance[next_node] = distance[current]+1
                q.append(next_node)

    return 0

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

    distance = [0] * (V+1)

    result = bfs(S)

    print(f"#{tc} {result}")