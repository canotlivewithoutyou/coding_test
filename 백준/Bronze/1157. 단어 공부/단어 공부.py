import sys

line=sys.stdin.readline().rstrip('\n')
line=line.upper()
nums=[0]*26
for ch in line:
    nums[ord(ch)-ord('A')]+=1

if nums.count(max(nums))>1:
    print("?")
else:
    print(chr(ord('A')+nums.index(max(nums))))