N = int(input())

nums = [input() for _ in range(N)]

def solution(a, b, c):
    s_a= a[::-1]
    s_b= b[::-1]
    s_c= c[::-1]

    for i in range(max(len(a), len(b), len(c))):
        n_a = int(s_a[i]) if i<len(s_a) else 0
        n_b = int(s_b[i]) if i<len(s_b) else 0
        n_c = int(s_c[i]) if i<len(s_c) else 0

        if n_a + n_b + n_c >= 10:
            return -1

    return int(a)+int(b)+int(c)


result = -1
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            result = max(result, solution(nums[i], nums[j], nums[k]))

print(result)

