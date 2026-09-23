N = int(input())

Rain=[]


for _ in range(N):
    year, day, weather = input().split()

    if weather=='Rain':
        Rain.append([year, day, weather])


Year = []
q,w,r=50000,30,30

answer=0
for i in range(len(Rain)):
    year = Rain[i][0]

    y = int(year[0:4]) #yyyy
    m = int(year[5:7])
    d = int(year[8:10])

    if y < q:
        answer=i
        q, w, r = y, m, d
    elif y==q:
        if m < w:
            answer = i
            q, w, r = y, m, d
        elif m == w:
            if d < r:
                answer = i
                q, w, r = y, m, d

print(*Rain[answer])