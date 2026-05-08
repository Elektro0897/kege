with open(r'./files/24_6757.txt') as file:
    data = file.readline()

data = data.replace('CFE', '*').replace('FCE', '*')
for i in set(data):
    if i != '*':
        data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))