import sys
max_num=-1
max_row=0
max_col=0
for i in range(9):
    row=list(map(int, sys.stdin.readline().split()))
    num=max(row)
    if num>max_num:
        max_num=num
        max_col=row.index(num)+1
        max_row=i+1
print(max_num)
print(max_row, max_col)