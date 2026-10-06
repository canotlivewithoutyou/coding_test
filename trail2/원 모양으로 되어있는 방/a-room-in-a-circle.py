N = int(input())

people=[0]*(N+1)
result = float('inf')

for i in range(1, N+1):
    people[i]=int(input())

def dist(start, target):
    if target >= start:
        return target-start
    else:
        return (N-start)+target

for start in range(1, N+1):
    current=0

    for target in range(1, N+1):
        distance = dist(start, target)
        current += distance*people[target]

    result = min(result, current)

print(result)