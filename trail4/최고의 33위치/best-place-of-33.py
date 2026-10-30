n = int(input())
maze = [list(map(int, input().split())) for _ in range(n)]

def solution(row_s, col_s, row_e, col_e):
    answer = 0

    for row in range(row_s, row_e+1):
        for col in range(col_s, col_e+1):
            answer+=maze[row][col]

    return answer

result = 0

for row in range(n):
    for col in range(n):
        
        if (row+2)>=n or (col+2)>=n:
            continue
        
        result = max(result, solution(row, col, row+2, col+2))

print(result)