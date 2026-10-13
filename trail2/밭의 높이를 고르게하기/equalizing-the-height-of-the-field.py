N, H, T = map(int, input().split())

inpt = list(map(int, input().split()))

def h(nums):
    re=0
    for hi in nums:
        re += abs(H-hi)
    return re

result = float('inf')

for start in range(N-T+1):
    result = min(result, h(inpt[start:start+T]))

print(result)

