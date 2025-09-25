k=int(input())
list_x, list_y=[],[]
for _ in range(k):
    a,b=map(int, input().split())
    list_x.append(a)
    list_y.append(b)
h=max(list_y)-min(list_y)
w=max(list_x)-min(list_x)
print(h*w)