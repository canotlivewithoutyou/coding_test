N, T = map(int, input().split())
conv1=list(map(int, input().split()))
conv2=list(map(int, input().split()))

for i in conv2:
    conv1.append(i)

for _ in range(T):
    temp = conv1[-1]
    for k in range(2*N-1, 0, -1):
        conv1[k]=conv1[k-1]
    conv1[0] = temp

idx=0
for _ in range(2):
    for _ in range(N):
        print(conv1[idx], end=' ')
        idx+=1
    print()

# 1 2 3 6 5 1 
# 