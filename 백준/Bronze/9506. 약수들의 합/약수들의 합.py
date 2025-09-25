import math
import sys

def measure(x):
    list=[]
    for i in range(1, math.ceil(math.sqrt(x))):
        if x%i==0:
            list.append(i)
            list.append(x//i)
    return list

def perfect(x,list):
    if (sum(list)-x)==x:
        list.sort()
        result=f"{x} = 1"
        for i in range(1,len(list)-1):
            result+=f" + {list[i]}"
        return result
    else:
        return f"{x} is NOT perfect."
        
for num in sys.stdin:
    num=int(num)
    if num==-1:
        exit()
    else:
        num_list=measure(num)
        print(perfect(num, num_list))
