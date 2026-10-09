N = int(input())

nums = list(map(int, input().split()))

cnt = 0

for start in range(N):
    current = 0
    length = 0 
    for end in range(start, N):
        length += 1
        current += nums[end]
        avr = current / length
        if avr in nums[start:end+1]:
            cnt+=1
    
print(cnt)
    