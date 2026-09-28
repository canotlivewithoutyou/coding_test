N = int(input())

points = []

for i in range(1, N + 1):
    x, y = map(int, input().split())

    dist = abs(x) + abs(y)

    # 거리와 점 번호를 같이 저장
    points.append((dist, i))

# 거리 기준으로 정렬
# 거리가 같으면 점 번호 기준으로 자동 정렬
points.sort()

for dist, num in points:
    print(num)