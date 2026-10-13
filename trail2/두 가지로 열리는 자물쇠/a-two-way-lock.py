N = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

def distance(start, end):
    max_num=max(start, end)
    min_num=min(start, end)

    r = max_num-min_num
    l = (N-max_num) + min_num

    return min(r, l)

def solve1(nums):
    for p in range(3):
        if distance(first[p], nums[p])>2:
            return False
    return True

def solve2(nums):
    for p in range(3):
        if distance(second[p], nums[p])>2:
            return False
    return True

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if solve1([i,j,k]) or solve2([i,j,k]):
                cnt +=1 

print(cnt)