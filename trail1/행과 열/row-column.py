n, m = map(int, input().split())

for i in range(1, n+1):
    num=i
    for _ in range(m):
        print(num,end=" ")
        num+=i
    print()