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
    edge = c - (i - 1)
    if edge < 0:
        print('')
    else:
        start = edge
        end = c + (i - 1)

    res.append(''.join(line))
print('\n'.join(res))
