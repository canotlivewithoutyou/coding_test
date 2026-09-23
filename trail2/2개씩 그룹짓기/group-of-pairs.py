N = int(input())
arr = list(map(int, input().split()))

def solution(arr,N):
    arr.sort()
    # arr = [2, 3, 5, 5]

    result=[]
    for i in range(N):
        result.append([arr[i], arr[-1-i]])
    
    answer=0
    for nums in result:
        if sum(nums)>answer:
            answer=sum(nums)

    return answer
        
print(solution(arr, N))