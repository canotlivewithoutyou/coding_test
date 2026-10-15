
from collections import deque

n = int(input())
q = deque()

for _ in range(n):
    command = input().split()

    if command[0] == 'push_back':
        q.append(int(command[1]))

    elif command[0] == 'get':
        print(q[int(command[1]) - 1])

    elif command[0] == 'size':
        print(len(q))

    elif command[0] == 'pop_back':
        q.pop()
