import sys

def result(list):
    if max(list)>=(sum(list)-max(list)):
        return "Invalid"
    else:
        if list[0]==list[1]==list[2]:
            return "Equilateral"
        elif list[0]!=list[1] and list[1]!=list[2] and list[0]!=list[2]:
            return "Scalene"
        else:
            return "Isosceles"

while 1:
    nums=list(map(int, sys.stdin.readline().split()))
    if sum(nums)==0: exit()
    print(result(nums))