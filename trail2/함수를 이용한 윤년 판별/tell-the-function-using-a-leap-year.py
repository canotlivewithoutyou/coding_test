def isYear(year):
    if year%4==0:
        if year%100==0 and year%400!=0:
            return 'false'
        else:
            return 'true'
    return 'false'

y = int(input())

print(isYear(y))