with open(r'./files/24_4682.txt') as file:
    data = file.readline()

data = data.replace('B', '*').replace('C', '*').replace('D', '*')
data = data.replace('A', '+').replace('E', '+')

ans = k = i = 0

while i < len(data) - 1:
    if data[i] + data[i + 1] == '+*':
        k += 1
        i += 2
    else:
        ans = max(ans, k)
        k = 0
        i += 1
ans = max(ans, k)
print(ans)