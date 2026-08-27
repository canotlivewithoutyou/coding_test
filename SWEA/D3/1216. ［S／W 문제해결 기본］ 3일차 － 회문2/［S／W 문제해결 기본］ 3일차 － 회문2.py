def solution(board, length):
    for row in board:
        for i in range(101 - length):
            word = row[i: i+length]
            
            if word == word[::-1]:
                return True
    return False

for _ in range(10):
    tc = int(input())
    
    board = [input() for _ in range(100)]
    T_board = ["".join(col) for col in zip(*board)]
    
    for length in range(100, 0, -1):
        if solution(board, length) or solution(T_board, length):
            answer = length
            break
    
    
    print(f'#{tc} {answer}')