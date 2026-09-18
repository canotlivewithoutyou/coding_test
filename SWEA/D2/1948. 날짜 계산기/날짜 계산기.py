T= int(input())

for tc in range(1, T+1):
    month1, day1, month2, day2 = map(int, input().split())

    days = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer=0
    for k in range(month1, month2+1):
        if k == month1:
            answer += days[k]-day1 +1
        elif k == month2:
            answer += day2
        else:
            answer+=days[k]
    print(f'#{tc} {answer}')