N, K, T =input().split()
N, K = int(N), int(K)

inpt = [input() for _ in range(N)]



def solution(arr, T):
    k = len(T)
    result=[]

    for string in inpt:
        isTrue=True
        if len(string)>=k:

            for i in range(k):
                if T[i]!=string[i]:
                    isTrue=False
    
            if isTrue:
                result.append(string)
    
    result.sort()
    return result


print((solution(inpt,T))[K-1])