import math

def prime_number(x):
    if x==1: return False
    for i in range(2,math.floor(math.sqrt(x))+1):
        if x%i==0 and i!=x:
            return False
    return True
result=[]
a,b=int(input()),int(input())
for k in range(a,b+1):
    if prime_number(k)==True:
        result.append(k)
    
if len(result)==0:
    print(-1)
else:
    print(sum(result))
    print(min(result))