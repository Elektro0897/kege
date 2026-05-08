with open(r'./files/24_4682.txt') as file:
    data = file.readline()

for i in data:
    if i in 'BCD':
        data = data.replace(i, '*')
    else:
        data = data.replace(i, '+')

ans = 0
for i in range(len(data) - 1):
    if data[i] + data[i + 1] == '+*':
        k = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j] + data[j + 1] == '+*':
                k += 1
            else:
                break
        ans = max(ans, k)
print(ans)