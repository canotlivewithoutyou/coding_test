import sys
n, b = sys.stdin.readline().split()
b=int(b)
digit=len(n)
res=0
for i in range(digit):
    ch=n[i]
    if 'A'<=ch<='Z':
        res+=int(ord(ch)-55)*(b**(digit-i-1))
    else:
        res+=int(ch)*(b**(digit-i-1))
print(res)