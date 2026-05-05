with open(r'../files/24_4627.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data) - 2):
    if data[i] + data[i + 1] + data[i + 2] in 'NPO PNO':
        k = 1
        for j in range(i + 3, len(data) - 2, 3):
            if data[j] + data[j + 1] + data[j + 2] in 'NPO PNO':
                k += 1
            else:
                break
        ans = max(ans, k)
print(ans)