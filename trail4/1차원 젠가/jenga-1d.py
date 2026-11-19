N = int(input())
block = [int(input()) for _ in range(N)]

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

block = block[:s1-1] + block[e1:]
block = block[:s2-1] + block[e2:]

print(len(block))
for num in block:
    print(num)
    

