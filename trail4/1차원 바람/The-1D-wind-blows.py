N, M, Q = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]


# 행 이동
def shift(row, d):
    if d == 'L':
        return row[-1:] + row[:-1]
    return row[1:] + row[:1]


# 반대 방향 반환
def reverse(d):
    return 'R' if d == 'L' else 'L'


# 인접한 두 행의 같은 열에 동일한 숫자가 있는지 확인
def can_spread(row1, row2):
    return any(a == b for a, b in zip(row1, row2))


# 바람 전파
def spread(r, d, step):
    nr = r + step

    while 0 <= nr < N:
        if not can_spread(maze[r], maze[nr]):
            break

        d = reverse(d)
        maze[nr] = shift(maze[nr], d)

        r = nr
        nr += step


for _ in range(Q):
    r, d = input().split()
    r = int(r) - 1

    maze[r] = shift(maze[r], d)

    spread(r, d, -1)  # 위쪽 전파
    spread(r, d, 1)   # 아래쪽 전파


for row in maze:
    print(*row)