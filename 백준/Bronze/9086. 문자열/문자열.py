import sys

a=int(input())
i=0
while i<a:
    line=list(sys.stdin.readline().rstrip('\n'))
    print(line[0]+line[-1])
    i+=1