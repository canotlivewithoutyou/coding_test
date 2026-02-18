from collections import deque

k=int(input())
queue=deque([i for i in range(1,k+1)])

while len(queue)!=1:
    queue.popleft()
    queue.rotate(-1)

print(*queue)