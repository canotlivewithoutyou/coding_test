inpt = list(map(int, input().split()))

l = len(inpt)
sums = sum(inpt)
result = float('inf')
for i in range(l):
    for j in range(i+1, l):
        for k in range(j+1, l):
            current = inpt[i]+inpt[j]+inpt[k]
            other = sums - current
            result = min(result, abs(current-other))

print(result)