N, M, Q = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

# 행 이동
def shift(row, direction):
    # 왼쪽에서 바람 -> 오른쪽 이동
    if direction == 'L':
        temp = row[-1]
        for i in range(M-1, 0, -1):
            row[i] = row[i-1]
        row[0] = temp

    # 오른쪽에서 바람 -> 왼쪽 이동
    elif direction == 'R':
        temp = row[0]
        for i in range(M-1):
            row[i] = row[i+1]
        row[-1] = temp

    return row

# -----

# 반대 방향 반환
def dire(direction):
    if direction == 'L':
        return 'R'
    elif direction == 'R':
        return 'L'

# -----

for _ in range(Q):
    r, d = input().split()
    r = int(r) - 1

    # 최초 바람이 불어오는 행 이동
    maze[r] = shift(maze[r], d)

    # 위쪽으로 전파
    direction = d

    for row in range(r, 0, -1):
        for i in range(M):
            if maze[row][i] == maze[row-1][i]:
                direction = dire(direction)
                maze[row-1] = shift(maze[row-1], direction)
                break
        else:
            break

    # 아래쪽으로 전파
    direction = d

    for row in range(r, N-1):
        for i in range(M):
            if maze[row][i] == maze[row+1][i]:
                direction = dire(direction)
                maze[row+1] = shift(maze[row+1], direction)
                break
        else:
            break


for row in maze:
    print(*row)