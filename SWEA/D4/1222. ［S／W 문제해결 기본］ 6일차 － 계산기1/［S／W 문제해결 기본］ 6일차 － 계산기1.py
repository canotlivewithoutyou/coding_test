for tc in range(1, 11):
    length = int(input())
    inpt = input()
    result = 0
    for k in range(0, length, 2):
        result+=int(inpt[k])
        
    print(f'#{tc} {result}')