with open(r'./files/24_4682.txt') as file:
    data = file.readline()

data = data.replace('B', '*').replace('C', '*').replace('D', '*')
data = data.replace('A', '+').replace('E', '+')
data = data.replace('+*', '-')
for i in set(data):
    if i != '-':
        data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))