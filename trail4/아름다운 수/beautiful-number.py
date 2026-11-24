N = int(input())
result=0

def solution(cnt):
    global result
    if cnt > N:
        return
    
    if cnt == N:
        result += 1
        return
    
    for k in range(1,5):
        solution(cnt+k)
    
solution(0)
print(result)