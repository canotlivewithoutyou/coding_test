import sys
rows, cols = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(rows)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(rows)]

for r in range(rows):
    summed = [A[r][c] + B[r][c] for c in range(cols)]
    print(*summed)
