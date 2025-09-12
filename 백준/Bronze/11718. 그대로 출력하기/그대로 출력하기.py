import sys

for line in sys.stdin:
    if not line.strip():
        continue
    print(line.rstrip('\n'))