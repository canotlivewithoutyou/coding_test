a=int(input())

def devide(x):
    for i in range(2,x+1):
        if x%i==0:
            return i

while a!=1:
    num=devide(a)
    print(num)
    a=a//num