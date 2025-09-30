import sys
x=int(input())
nums=[]
for line in range(x):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for i in nums:
    print(i)