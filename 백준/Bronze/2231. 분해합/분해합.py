a= int(input())
a_len=len(str(a))
start=a-9*a_len if a>18 else 1
end=a

def sum(x):
    result=0
    for i in str(x):
        result+=int(i)
    return result

for i in range(start,end):
    if i+sum(i)==a:
        print(i)
        exit()
print(0)