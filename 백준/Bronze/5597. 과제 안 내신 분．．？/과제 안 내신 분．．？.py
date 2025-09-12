import sys
nums=[]
result=[]
for line in sys.stdin:
    if not line.strip():
        continue
    nums.append(int(line.strip()))

for i in range(1,31):
    if i not in nums:
        result.append(i)
print(min(result))
print(max(result))