import sys
k=int(sys.stdin.readline())
for _ in range(k):
    a, b = sys.stdin.readline().split()
    result=[]
    for ch in b:
        result.append(ch*int(a))
    print(''.join(result))