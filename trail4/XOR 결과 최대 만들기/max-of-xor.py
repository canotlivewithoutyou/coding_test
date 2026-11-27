N, M = map(int, input().split())
nums = list(map(int, input().split()))

scores = []
result = 0

def xor(arr):
    value = 0
    for num in arr:
        value ^= num
    return value

def solution(start):
    global result
    
    if len(scores) == M:
        result = max(result, xor(scores))
        return 
    
    for i in range(start, N):
        scores.append(nums[i])
        solution(i+1)
        scores.pop()

solution(0)

print(result)