import sys

a,b=map(int, sys.stdin.readline().split())
matrix1=[list(map(int, sys.stdin.readline().split())) for _ in range(a)]
b,c=map(int, sys.stdin.readline().split())
matrix2=[list(map(int, sys.stdin.readline().split())) for _ in range(b)]

result=[[0]*c for _ in range(a)]

for i in range(a):
    for j in range(c):
        acc=0
        for k in range(b):
            acc+=matrix1[i][k]*matrix2[k][j]
        result[i][j]=acc

for rows in result:
    print(*rows)