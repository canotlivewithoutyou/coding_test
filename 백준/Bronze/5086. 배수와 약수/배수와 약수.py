import sys

def result(a,b):
    if a<b and b%a==0:
        print("factor")
    elif a>b and a%b==0:
        print("multiple")
    else:
        print("neither")

for line in sys.stdin:
    a,b=map(int, line.split())
    if a==0 and b==0:
        exit()
    else:
        result(a,b)