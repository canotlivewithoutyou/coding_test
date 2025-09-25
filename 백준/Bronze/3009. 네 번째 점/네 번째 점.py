list_x=[]
list_y=[]
for i in range(3):
    a,b=map(int,input().split())
    if a in list_x:
        list_x.remove(a)
    else: 
        list_x.append(a)
    if b in list_y:
        list_y.remove(b)
    else: 
        list_y.append(b)

print(*list_x, *list_y)