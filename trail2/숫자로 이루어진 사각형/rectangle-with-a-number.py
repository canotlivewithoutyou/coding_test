n = int(input())

# Please write your code here.

maze =[[0]*n for _ in range(n)]

k=1
for i in range(n):
    for j in range(n):
        maze[i][j]=k
        k+=1
        if k>9:
            k=1
    
    

for row in maze:
    print(*row)