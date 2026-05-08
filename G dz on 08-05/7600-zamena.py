with open(r'./files/24_7600.txt') as file:
    data = file.readline()
for i in 'QSR':
    data = data.replace(i, '*')
data = data.replace('**', ' ')
data = data.split()
print(len(max(data, key=len)))