N = int(input())

# 현재 위치
pos = 0

# 각 위치별 [흰색 횟수, 검은색 횟수, 마지막 색]
tiles = {}

for _ in range(N):
    x, d = input().split()
    x = int(x)

    # 이동할 방향
    if d == 'L':
        move = -1
        color = 'W'
    else:
        move = 1
        color = 'B'

    # 현재 위치 포함해서 x칸 칠하기
    for _ in range(x):
        if pos not in tiles:
            tiles[pos] = [0, 0, '']

        if color == 'W':
            tiles[pos][0] += 1
        else:
            tiles[pos][1] += 1

        tiles[pos][2] = color

        # 마지막 칸에서는 이동하지 않음
        if _ != x - 1:
            pos += move


white = 0
black = 0
gray = 0

for w, b, last in tiles.values():

    # 흰색, 검은색 둘 다 2번 이상
    if w >= 2 and b >= 2:
        gray += 1

    # 회색이 아니라면 마지막 색깔
    elif last == 'W':
        white += 1

    else:
        black += 1

print(white, black, gray)