n = 3 * 2
result = []

c = n // 2
end = c - 1
start = end
for i in range(n):
    k = 1
    line = [' '] * (n - 1)
    for j in range(start, end + 1):
        if i == c - 1:
            start = end
        if i > c - 1:
            line[-j] = str(k)
        else:
            line[j] = str(k)
        k = k + 1
    result.append(''.join(line))

    start = start - 1
print('\n'.join(result))
