res = []
n = 3 * 2
for i in range(n):
    if i == 0:
        continue
    line = [' '] * (n - 1)
    c = len(line) // 2
    if i == 1:
        line[c] = str(i)
        continue

    if c > i:
        start = c - (i - 1)
        end = c + (i - 1)
    else:
        print('')

    res.append(''.join(line))
print('\n'.join(res))
