N, K = map(int, input().split())

inpt = []
max_xi = 0
for _ in range(N):
    a, b = input().split()
    max_xi=max(max_xi, int(a))
    inpt.append([a,b])

rocation = [0]*(max_xi+1)

# 배열에 저장
for roc, alpha in inpt:
    roc = int(roc)
    if alpha == 'G':
        rocation[roc] = 1
    elif alpha == 'H':
        rocation[roc] = 2

result = 0

if max_xi<=K:
    result = sum(rocation)

for k in range(1, max_xi-K+1):
    current = sum(rocation[k: k+K+1])
    result = max(current, result)

print(result)

