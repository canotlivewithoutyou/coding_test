def solve():
    # 1. A진수와 B진수 입력 받기
    A, B = map(int, input().split())
    
    # 2. A진수로 표현된 수 N을 문자열로 입력 받기
    N = input().strip()
    
    # 3. A진수 수 N을 10진수 정수로 변환
    decimal_number = int(N, A)
    
    # 4. 10진수 정수를 B진수 문자열로 변환
    if decimal_number == 0:
        print(0)
        return
        
    result = []
    while decimal_number > 0:
        remainder = decimal_number % B
        # 만약 B가 10보다 커서 문자가 필요한 경우를 대비 (예: 10->'A', 11->'B' ...)
        if remainder >= 10:
            result.append(chr(ord('A') + remainder - 10))
        else:
            result.append(str(remainder))
        decimal_number //= B
        
    # 역순으로 정렬하여 출력
    print(''.join(reversed(result)))

if __name__ == '__main__':
    solve()