T = int(input())

for _ in range(T):
    tc, tc_len = map(str, input().split())
    inpt = list(map(str, input().split()))
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    
    count = dict.fromkeys(nums, 0)
    
    for i in inpt:
        count[i]+=1
    
    result = []
    
    for item, value in count.items():
        for _ in range(value):
            result.append(item)
    
    print(tc)
    print(" ".join(result))