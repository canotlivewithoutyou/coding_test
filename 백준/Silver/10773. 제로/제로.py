import sys

result=[]
a=int(input().strip())

for k in range(a):
    k=int(sys.stdin.readline().strip())
    if k==0:
        result.pop()
    else:
        result.append(k)

print(sum(result))