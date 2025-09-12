import sys
line=sys.stdin.readline().strip()
for c in range(ord('a'), ord('z')+1):
    print(line.find(chr(c)), end=" ")