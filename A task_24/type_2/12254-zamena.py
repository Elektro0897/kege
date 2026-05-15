with open(r'../files/24_12254.txt') as file:
    data = file.readline()

data = data.replace('RSQ', '***')
data = data.replace('SQ*', ' ***').replace('Q*', ' **')
data = data.replace('*RS', '*** ').replace('*R', '** ')
for i in set(data):
    if i != '*':
        data = data.replace(i, ' ')
data = data.split()

print(len(max(data, key=len)))
