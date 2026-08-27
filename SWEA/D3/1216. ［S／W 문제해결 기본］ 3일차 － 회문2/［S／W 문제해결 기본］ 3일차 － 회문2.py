def solution(inpt, k):
    for row in inpt:
        current_len = 100-k
        for i in range(100-current_len+1):
            see = row[i:i+current_len]
            if see == see[::-1]:
                return current_len
    return 0

for _ in range(10):
    tc = int(input())
    
    inpt = [input() for _ in range(100)]
    T_inpt = ["".join(col) for col in zip(*inpt)]
    
    max_len, origin_max, T_max, current_len = 0, 0, 0, 0
    
    for j in range(100):
        current_len=solution(inpt, j)
        if origin_max < current_len:
            origin_max = current_len
        if origin_max !=0:
            break
    
    for j in range(100):
        current_len=solution(T_inpt, j)
        if T_max < current_len:
            T_max = current_len
        if T_max != 0:
            if T_max <= origin_max:
                max_len = origin_max
                break
            else:
                if T_max > origin_max:
                    max_len = T_max
                    break
                    
    print(f'#{tc} {max_len}')