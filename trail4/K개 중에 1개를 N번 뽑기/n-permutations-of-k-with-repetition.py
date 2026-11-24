K, N = map(int, input().split())

nums=[]

def result():
    for num in nums:
        print(num, end=' ')
    print()

def solution(cnt):

    if cnt == N:
        result()
        return 

    for i in range(1, K+1):
        nums.append(i)
        solution(cnt+1)
        nums.pop()

solution(0)


