N = int(input())

maze = [list(map(int, input().split())) for _ in range(N)]

result = 0

for col in range(N):
    for row in range(N-2):
        result = max(result, maze[col][row]+maze[col][row+1]+maze[col][row+2])

    if result==3:
        break

print(result)