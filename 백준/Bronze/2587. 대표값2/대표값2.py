import sys
def average(list):
    return sum(list)//len(list)

def center(list):
    list.sort()
    return list[2]

nums=[]
for line in sys.stdin:
    if not line.strip:
        continue
    nums.append(int(line.rstrip()))

print(average(nums))
print(center(nums))