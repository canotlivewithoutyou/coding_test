N, T = map(int, input().split())
conv=[]
for _ in range(3):
    arr = list(map(int, input().split()))
    conv.extend(arr)

for _ in range(T):
    temp = conv[-1]
    for k in range(3*N-1, 0, -1):
        conv[k] = conv[k-1]
    conv[0] = temp

print(*conv[:N])
print(*conv[N:2*N])
print(*conv[2*N:])