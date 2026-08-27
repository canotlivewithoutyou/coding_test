def solution(inpt):
    if inpt == inpt[::-1]:
        return 1
    else:
        return 0

T = int(input())

for tc in range(1, T + 1):
    
    inpt = input()
    
    print(f'#{tc} {solution(inpt)}')