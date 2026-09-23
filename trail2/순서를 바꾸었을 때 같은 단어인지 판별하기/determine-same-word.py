
def solution(string):
    result=[]

    for ch in string:
        result.append(ch)
    result.sort()
    return result

str1= input()
str2=input()

m1 = solution(str1)
m2 = solution(str2)

if m1==m2:
    print("Yes")

else:
    print("No")