n,k =map(int, input().split())
result, num = 0,0
for i in range(1,n+1):
    if n%i==0:
        result=i
        num+=1
        if num==k:
            print(result)
            exit()
print(0)