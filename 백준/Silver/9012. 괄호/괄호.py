import sys

T=int(input())

for _ in range(T):
    data=sys.stdin.readline().strip()
    result=[]
    ok=True
    for ch in data:
        if ch=='(':
            result.append(ch)
        elif ch==')' and len(result)>0:
            result.pop()
        else:   #stack안에 '('가 없는 경우 -> NO
            ok=False
            break
    if ok and not result: 
        print("YES") 
    else: 
        print("NO")