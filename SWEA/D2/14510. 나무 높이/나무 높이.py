T = int(input())

for tc in range(1, T+1):
    N = int(input())
    height = list(map(int, input().split()))

    mh = max(height)

    one, two = 0, 0

    for h in height:
        diff = mh - h

        one += diff%2
        two += diff//2

    while two>one+1:
        one+=2
        two-=1

    if one>two:
        answer=one*2-1
    else:
        answer=two*2

    print(f"#{tc} {answer}")