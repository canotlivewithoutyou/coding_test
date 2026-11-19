N, T = map(int, input().split())
conv1=list(map(int, input().split()))
conv2=list(map(int, input().split()))
conv1.extend(conv2)

for _ in range(T):
    temp = conv1[-1]
    for k in range(2*N-1, 0, -1):
        conv1[k]=conv1[k-1]
    conv1[0] = temp

idx=0
print(*conv1[:N])
print(*conv1[N:])