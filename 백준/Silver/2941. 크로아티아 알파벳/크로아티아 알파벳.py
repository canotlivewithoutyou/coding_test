import sys

line=sys.stdin.readline().rstrip('\n')
result=0
i=0
two=["c=", "c-", "d-", "lj", "nj", "s=", "z="]

while i<len(line):
    if line[i:i+3]=="dz=":
        result+=1
        i+=3
    elif line[i:i+2] in two:
        result+=1
        i+=2
    else:
        result+=1
        i+=1
print(result)