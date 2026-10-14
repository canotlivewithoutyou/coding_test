n = 6
arr = list(map(int, input().split()))

min_re = float('inf')

def diff(i, j, k, l):
    sum1 = arr[i]+arr[j]
    sum2 = arr[k]+arr[l]
    sum3 = sum(arr) - (sum1+sum2)

    mmax = max(sum1, sum2, sum3)
    mmin = min(sum1, sum2, sum3)
    return mmax - mmin

for i in range(n):
    for j in range(1+i, n):

        for k in range(n):
            for l in range(k+1, n):
                if k==i or k==j or l==i or l==j:
                    continue
                min_re = min(min_re, diff(i,j,k,l))

print(min_re)