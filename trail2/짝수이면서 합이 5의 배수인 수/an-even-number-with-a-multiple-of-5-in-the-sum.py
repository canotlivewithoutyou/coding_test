n = input()

result=0
for ch in n:
    result += int(ch)

if int(n)%2==0 and result%5==0:
    print("Yes")
else:
    print("No")