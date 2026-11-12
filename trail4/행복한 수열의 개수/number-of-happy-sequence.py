N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
T_maze = [list(col) for col in zip(*maze)]
result = 0

def is_happy_sequence(seq):
    cnt=1
    if cnt>=M:
        return True
        
    for i in range(0, N-1):
        if seq[i]==seq[i+1]:
            cnt+=1
        else:
            cnt=1
    
        if cnt>=M:
            return True
    
    return False
    
for i in range(N):
    seq1 = maze[i][:]
    seq2 = T_maze[i][:]
    if is_happy_sequence(seq1):
        result += 1

    if is_happy_sequence(seq2):
        result+=1

print(result)