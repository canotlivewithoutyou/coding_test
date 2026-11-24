# K이하의 정수를 하나 고르는 행위를 N번 반복하여 나올 수 있는 모든 서로 다른 수열을 구하는 프로그램
K, N = map(int, input().split())
    
answer = []

def solution():

    # 종료 조건
    if len(answer)==N:
        print(*answer)
        return 

    for i in range(1, K+1):

        if len(answer)>=2 and answer[-1]==answer[-2]==i:
            continue

        answer.append(i)
        solution()
        answer.pop()
    
solution()

