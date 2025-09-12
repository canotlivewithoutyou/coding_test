x=int(input())
for i in range(1, 2*x):
    if x-i>=0:
        print(" "*(x-i)+"*"*(2*i-1))
    else:
        print(" "*(i-x)+"*"*(2*(2*x-i)-1))