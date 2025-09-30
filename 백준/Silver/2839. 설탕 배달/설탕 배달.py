x=int(input())
if x>=5:
    a=x//5
    for i in range(a,-1,-1):
        if i!=0:
            b=x-(5*i)
            if b%3==0:
                print(i+(b//3))
                exit()
        else:
            if x%3==0:
                print(x//3)
                exit()
    
else:
    if x%3==0:
        print(x//3)
        exit()
print(-1)