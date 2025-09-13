import sys

matrix=[sys.stdin.readline().rstrip('\n') for _ in range(5)]
max_len=0
result=''
for i in range(5):
    max_len=max(len(matrix[i]), max_len)

for j in range(max_len):
    for k in range(5):
        if j<len(matrix[k]) and matrix[k][j]!=' ':
            result+=matrix[k][j]
print(result)