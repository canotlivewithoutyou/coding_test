import sys
rows, cols = map(int, sys.stdin.readline().split())
matrix1=[list(map(int, sys.stdin.readline().split())) for _ in range(rows)]
matrix2=[list(map(int, sys.stdin.readline().split())) for _ in range(rows)]

for i in range(rows):
    sum=[matrix1[i][j]+matrix2[i][j] for j in range(cols)]
    print(*sum)