
N, K = map(int, input().split())

inpt = []
max_xi = 0

for _ in range(N):
    sugar, idx = map(int, input().split())
    inpt.append([idx, sugar])
    max_xi = max(max_xi, idx)

sugars = [0] * (max_xi + 1)

for idx, sugar in inpt:
    sugars[idx] += sugar

# 구간의 길이
window = 2 * K + 1

# 첫 번째 구간의 사탕 합
current = sum(sugars[:window])
result = current

# 슬라이딩 윈도우
for i in range(window, len(sugars)):
    current += sugars[i]
    current -= sugars[i - window]
    result = max(result, current)

print(result)
