N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

def area(k):
    return k**2 + (k+1)**2

def get_num_of_gold(row, col, k):
    answer = 0

    for i in range(N):
        for j in range(N):
            if (abs(row-i)+abs(col-j)) <= k:
                answer += maze[i][j]
    return answer

result = 0

for row in range(N):
    for col in range(N):
        for k in range(2*(N-1)+1):
            num_of_gold = get_num_of_gold(row, col, k)

            if num_of_gold*M >= area(k):
                result = max(result, num_of_gold)

print(result)