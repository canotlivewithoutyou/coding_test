N, K=map(int, input().split())
arr=[k for k in range(1,N+1)]

result=[] #제거된 사람을 넣을 배열
num=0 #제거될 사람의 인덱스 번호

for _ in range(N):
    num += K-1
    if num>=len(arr): #한 바퀴를 돌고 그 다음으로 돌아갈 때를 대비하여 값을 나머지로 바꿔줌 
        num=num%len(arr)

    result.append(str(arr.pop(num)))

print("<",", ".join(result)[:],">", sep='')