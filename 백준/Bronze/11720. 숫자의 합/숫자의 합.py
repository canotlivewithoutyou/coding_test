import sys
a=input()
result=0
nums=list(sys.stdin.readline().rstrip('\n'))
for i in nums:
    result+=int(i)
print(result)