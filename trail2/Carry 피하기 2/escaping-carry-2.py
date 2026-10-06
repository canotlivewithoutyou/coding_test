N = int(input())

nums = [input() for _ in range(N)]

def solution(a, b, c):
    max_len= max(len(a), len(b), len(c))

    a = a.zfill(max_len)
    b = b.zfill(max_len)
    c = c.zfill(max_len)

    for i in range(max_len):
        if int(a[i])+int(b[i])+int(c[i]) >= 10:
            return -1

    return int(a)+int(b)+int(c)


result = -1
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            result = max(result, solution(nums[i], nums[j], nums[k]))

print(result)

