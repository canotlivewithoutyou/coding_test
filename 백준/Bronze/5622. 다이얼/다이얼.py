import sys

groups = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
line=sys.stdin.readline().strip()
result=0
for ch in line:
    for a, b in enumerate(groups):
        if ch in b:
            result+=a+2+1
            break
print(result)