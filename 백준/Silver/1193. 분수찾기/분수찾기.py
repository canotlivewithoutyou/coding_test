x=int(input())
line=1
while x>line:
    x=x-line
    line+=1

if line%2==0:
    a,b=x, line-x+1
else:
    a,b=line-x+1, x
print(f"{a}/{b}")