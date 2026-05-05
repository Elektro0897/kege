with open(r'../files/24_4627.txt') as file:
    data = file.readline()

ans = k = i = 0

while i < len(data) - 2:
    if data[i] + data[i + 1] + data[i + 2] in 'PNO NPO':
        k += 1
        i += 3
    else:
        ans = max(ans, k)
        k = 0
        i += 1
ans = max(ans, k)
print(ans)
