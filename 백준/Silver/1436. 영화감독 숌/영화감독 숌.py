x=int(input())
i, result = 0,666

while True:
    if '666' in str(result):
        i+=1
    
    if i==x:
        break

    result+=1
print(result)