a, b = map(int, input().split())

def solution(x,y):
    result=[]
    for i in range(x,y+1):
        if i%3==0:
            result.append(i)
        else:
            if isIn(i):
                result.append(i)
    
    return len(set(result))

def isIn(x):
    for ch in str(x):
        if ch=='3' or ch =='6' or ch=='9':
            return True
    return False

print(solution(a,b))