N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

# 가능한 모든 모양
shapes = [
    [[1,1,0],
    [1,0,0],
    [0,0,0]],

    [[1,1,0],
    [0,1,0],
    [0,0,0]],

    [[0,1,0],
    [1,1,0],
    [0,0,0]],

    [[1,0,0],
    [1,1,0],
    [0,0,0]], 

    [[1,1,1],
    [0,0,0],
    [0,0,0]],

    [[1,0,0],
    [1,0,0],
    [1,0,0]],
]

def solution(x, y):
    max_sum = 0

    for i in range(6):

        is_possible = True
        sum_of_num = 0

        for dx in range(3):
            for dy in range(3):
                if not shapes[i][dx][dy]:
                    continue
                
                # idx범위를 벗어난다면 false
                if (x+dx>=N) or (y+dy>=M):
                    is_possible=False
                else: 
                    sum_of_num += maze[x+dx][y+dy]
                
            if is_possible:
                max_sum = max(max_sum, sum_of_num)

    return max_sum

answer = 0

for i in range(N):
    for j in range(M):
        answer = max(answer, solution(i, j))

print(answer)