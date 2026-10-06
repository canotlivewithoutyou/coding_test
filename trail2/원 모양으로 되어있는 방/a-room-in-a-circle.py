N = int(input())

arr = [0]*(N+1)

for i in range(1,N+1):
    arr[i] = int(input())


def dist(start, target):

    if target>=start:
        return target-start
    else:
        return (N-start)+target

result = float('inf')

for start in range(1, N+1):
    current = 0
    for target in range(1, N+1):
        distance = dist(start, target)
        current += distance*arr[target]

    result = min(result, current)

print(result)