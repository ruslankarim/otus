res = []
n = 5 * 2
for i in range(n):
    if i == 0:
        continue
    line = [' '] * (n - 1)
    c = len(line) // 2
    k = 1
    if i == 1 or i == len(line):
        start = c
        end = start
    elif c + 1 < i:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
    for j in range(start, end + 1):
        line[j] = str(k)
        if j >= c:
            k = k - 1
        else:
            k = k + 1
    res.append(''.join(line))
print('\n'.join(res))
