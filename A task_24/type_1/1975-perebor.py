with open(r'../files/24_1975.txt') as file:
    data = file.readline()

k = 1
ans = 0
for i in range(len(data)-1):
    if data[i:i + 2] != 'PP':
        k += 1
    else:
        if ans < k: ans = k
        k = 1
if ans < k: ans = k
print(ans)