nums=list(map(int, input().split()))
nums.sort()
a,b,c=nums[0],nums[1],nums[2]

if c<a+b:
    print(a+b+c)
else:
    print(2*(a+b)-1)