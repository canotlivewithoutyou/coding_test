N = int(input())

inpt = list(map(int, input().split()))

result = []

for i in range(0, N, 2):
    answer=inpt[0:i+1]
    answer.sort()
    result.append(answer[(i+1)//2])

print(*result)