import sys
k=int(sys.stdin.readline())
result=0

for _ in range(k):
    text=sys.stdin.readline().rstrip('\n')
    seen=set()
    prev=None

    for ch in text:
        if ch == prev:
            continue
        if ch in seen:
            break
        seen.add(ch)
        prev=ch
    else:
        result+=1
print(result)