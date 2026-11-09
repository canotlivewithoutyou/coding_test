s = input().strip()
count = 0

for ch in s:
    if ch == '(':
        count += 1
    else:
        count -= 1

    if count < 0:
        break

print("Yes" if count == 0 else "No")