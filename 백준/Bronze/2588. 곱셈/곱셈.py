a=int(input())
b=[int(x) for x in input()]
c=[]
for i in range(2,-1,-1):
    c.append(a*b[i])
    print(a*b[i])
print(c[0]+c[1]*10+c[2]*100)