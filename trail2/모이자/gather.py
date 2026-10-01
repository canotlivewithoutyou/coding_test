N = int(input())

nums = list(map(int, input().split()))

def solution(k):
    dist = 0
    for idx in range(N):
        if idx>k:
            dist += (idx-k)*nums[idx]
        else:
            dist+= (k-idx)*nums[idx]
    return dist

result = float('inf')
for k in range(N):
    distance = solution(k)
    if result>distance:
        result= distance

print(result)