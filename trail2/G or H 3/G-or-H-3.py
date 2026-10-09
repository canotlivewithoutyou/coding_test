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

current = sum(rocation[1:K+2])
result = current

for right in range(K+2, max_xi+1):
    # 왼쪽 값 하나 빼기
    current -= rocation[right-K-1]

    # 오른쪽 값 하나 빼기
    current += rocation[right]

    # result 갱신
    result = max(result, current)

print(result)
