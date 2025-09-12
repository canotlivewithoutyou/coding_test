nums=[]
k, j =0, 0
for i in range(9):
    nums.append(int(input()))
for q in range(9):
    if nums[q]>k:
        k=nums[q]
        j=q+1
print(k)
print(j)