import sys

line=sys.stdin.readline().rstrip('\n')
if len(line)%2==0:
    if line[:len(line)//2]==line[len(line)//2:][::-1]:
        print(1)
    else:
        print(0)
else:
    if line[:len(line)//2]==line[len(line)//2+1:][::-1]:
        print(1)
    else:
        print(0)
