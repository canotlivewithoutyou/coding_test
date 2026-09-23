A, B = map(int, input().split())

def solution(x, y):
    result=0
    for k in range(x, y+1):
        if isTrue(k):
            result+=k
    return result



def isTrue(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

print(solution(A,B))