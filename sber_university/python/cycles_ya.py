res = []
n = 3 * 2
for i in range(n):
    if i == 0:
        continue
    line = [' '] * (n - 1)
    c = len(line) // 2
    start = 0
    end = len(line) - 1
    k = 1
    if i == 1 or i == len(line):
        start = c
        end = start + 1
    elif c + 1 < i:
        start += 1
        end -= 1
    else:
        start = c - (i - 1)
        end = c + (i - 1)
    for j in range(start, end):
        if j < c:
            k = k + 1
        elif j > c:
            k = k - 1
        line[j] = str(k)
    res.append(''.join(line))
print('\n'.join(res))
