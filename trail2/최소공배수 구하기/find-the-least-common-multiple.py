n, m = map(int, input().split())

# Please write your code here.

for i in range(max(n,m),156484342,max(n,m)):
    if i%n==0 and i%m==0:
        print(i)
        break