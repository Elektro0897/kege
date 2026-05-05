with open(r'../files/24_4627.txt') as file:
    data = file.readline()

data = data.replace('NPO', '+').replace('PNO', '+')
for i in set(data):
    if i != '+':
        data = data.replace(i, ' ')
data = data.split()

print(len(max(data, key=len)))