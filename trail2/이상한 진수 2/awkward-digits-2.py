inpt = list(input())

isChanged = False

for i in range(len(inpt)):
    if inpt[i]=="0":
        inpt[i]="1"
        isChanged = True
        break
    
if not isChanged:
    inpt[-1]="0"


result = 0
i=len(inpt)-1

for k in inpt:
    
    if k=="1":
        result += 2**i
    
    i-=1

print(result)