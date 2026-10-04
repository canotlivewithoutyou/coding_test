x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

width = x2 - x1
height = y2 - y1

answer = width * height

# 두 번째 직사각형이 첫 번째 직사각형을 완전히 덮는 경우
if a1 <= x1 and a2 >= x2 and b1 <= y1 and b2 >= y2:
    answer = 0

# 첫 번째 직사각형의 세로 전체를 덮는 경우
elif b1 <= y1 and b2 >= y2:

    # 왼쪽에서 덮음
    if a1 <= x1 and a2 > x1:
        answer = max(0, x2 - a2) * height

    # 오른쪽에서 덮음
    elif a2 >= x2 and a1 < x2:
        answer = max(0, a1 - x1) * height

# 첫 번째 직사각형의 가로 전체를 덮는 경우
elif a1 <= x1 and a2 >= x2:

    # 아래쪽에서 덮음
    if b1 <= y1 and b2 > y1:
        answer = width * max(0, y2 - b2)

    # 위쪽에서 덮음
    elif b2 >= y2 and b1 < y2:
        answer = width * max(0, b1 - y1)

print(answer)