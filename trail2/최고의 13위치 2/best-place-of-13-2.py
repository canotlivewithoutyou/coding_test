N= int(input())

board = [list(map(int, input().split())) for _ in range(N)]

rects = []

for r in range(N):
    for c in range(N-2):
        coin = board[r][c] + board[r][c+1] + board[r][c+2]

        rects.append((r, c, coin))

answer = 0

for i in range(len(rects)):
    r1, c1, coin1 = rects[i]

    for j in range(i+1, len(rects)):
        r2, c2, coin2 = rects[j]

        if r1 != r2 :
            answer = max(answer, coin1+coin2)
        elif abs(c1-c2)>=3:
            answer = max(answer, coin1+coin2)
        
        if answer==6:
            break
    if answer==6:
        break

print(answer)


