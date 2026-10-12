N = int(input())

inpt = []
max_idx = 0
for _ in range(N):
    idx, gh = input().split()
    idx = int(idx)
    max_idx = max(max_idx, idx)
    inpt.append([idx, gh])

arr = [0]*(max_idx+1)

for idx, gh in inpt:
    arr[idx] = gh


def solution():

    # length = 구간의 크기 (하나씩 줄이면서 봄)
    for length in range(max_idx+1, 0, -1):

        for end in range(max_idx, length-2, -1):

            start = end-length+1

            current = arr[start:end+1]
            
            g,h=0,0

            if current[0]==0 or current[-1]==0:
                continue

            for k in current:
                if k =='G':
                    g+=1
                elif k == 'H':
                    h+=1
            
            if (g>0 and h==0) or (h>0 and g==0) or (h==g and h>0 and g>0):
                return end-start
    return 0

result = solution()  

print(result)
