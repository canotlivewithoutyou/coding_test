a,b=map(int,input().split())
while(1):
    if a==b:
        print("==")
        break
    elif a>b:
        print(">")
        break
    else:
        if a<b:
            print("<")
            break