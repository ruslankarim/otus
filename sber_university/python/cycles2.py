n = 3 * 2
result = []

c = n // 2
end = c - 1
start = end
for i in range(n):
    k = 1
    line = [' '] * (n - 1)
    for j in range(start, end + 1):
        line[j] = str(k)
        result.append(''.join(line))
        k = k + 1
    start = start - 1
print('\n'.join(result))
