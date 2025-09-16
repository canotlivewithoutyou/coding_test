import sys

n=int(input())

map_array=[[0]*100 for _ in range(100)]
result=0
for _ in range(n):
    x, y = map(int,sys.stdin.readline().split())
    
    for i in range(y, y+10):
        idx_x=i
        for j in range(x, x+10):
            idx_y=j
            if map_array[idx_y][idx_x]==0:
                map_array[idx_y][idx_x]=1

for i in range(100):
    result+=sum(map_array[i])
print(result)