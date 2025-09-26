a1, a0=map(int, input().split())
c=int(input())
num=int(input())

#기울기가 같고, a0=0이면 false
if a1==c:
    if a0>0: print(0)
    else: print(1)
#함수 g의 기울기가 f보다 클 때 
elif a1>c:
    print(0)
#기울기가 다를때
else:
    point=-(a0/(a1-c))
    if point<=num: print(1)
    else: print(0)