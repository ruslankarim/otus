
sum = 0
for i in [758, 483, 893, 393, 293, 292, 292, 485, 828, 182]:
    sum = sum + i

# print(sum)

num_zeroes = 0

for i in [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]:
    if i == 0:
        num_zeroes = num_zeroes + 1

# print(num_zeroes)

res = []
for i in range(3):
    i = i + 1
    if i == 0:
        continue
    line = []
    for j in range(i):
        line.append(str(j + 1))
    res.append(''.join(line))
# print('\n'.join(res))

res = []
n = 3
for i in range(n + 1):
    if i == 0:
        continue
    line = [' '] * (n * 2 - 1)
    c = len(line) // 2
    offset = i - 1
    start = c - offset
    end = c + offset
    if start == c:
        line[c] = str(i)
    else:
        k = 1
        for j in range(start, end + 1):
            line[j] = str(k)
            if j < c:
                k = k + 1
            else:
                k = k - 1
    res.append(''.join(line))
# print('\n'.join(res))

res = []
n = 5
for i in range(n * 2):
    if i == 0:
        continue
    line = [' '] * (n * 2 - 1)
    c = len(line) // 2
    offset = i - 1
    if c - (i - 1) == c:
        line[c] = str(i)
    else:
        k = 1
        if i > c + 1:
            start = start + 1
            end = end - 1
            for j in range(start, end + 1):
                line[j] = str(k)
                if j >= c:
                    k = k - 1
                else:
                    k = k + 1
        else:
            start = c - offset
            end = c + offset
            for j in range(start, end + 1):
                line[j] = str(k)
                if j < c:
                    k = k + 1
                else:
                    k = k - 1
    res.append(''.join(line))
print('\n'.join(res))

