import sys
nums=[]
i=0
while i!=10:
    a=int(input())
    if a%42 not in nums:
        nums.append(a%42)
    i+=1
print(len(nums))