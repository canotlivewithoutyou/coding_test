n = 5
arr = list(map(int, input().split()))

result = float('inf')

def solution(i, k, l):
    sum1 = arr[i]
    sum2 = arr[k]+arr[l]
    sum3 = sum(arr) - (sum1+sum2)
    if sum1 == sum2 or sum1 == sum3 or sum2 == sum3:
        return float('inf')
    mmax = max(sum1, sum2, sum3)
    mmin = min(sum1, sum2, sum3)
    return mmax-mmin



for i in range(n):

    for k in range(n):
        for l in range(1+k, n):
            if i==k or i==l:
                continue
            result = min(result, solution(i, k, l))

if result == float('inf'):
    print(-1)
else:
    print(result)
