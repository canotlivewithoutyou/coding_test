nums=list(map(int, input().split()))
nums.sort(reverse=True)
if nums[0]==nums[1]==nums[2]:
    print(10000+nums[0]*1000)
elif nums[0]==nums[1]:
    print(nums[0]*100+1000)
elif nums[1]==nums[2]:
    print(nums[1]*100+1000)
elif nums[2]==nums[0]:
    print(nums[2]*100+1000)
else:
    print(nums[0]*100)