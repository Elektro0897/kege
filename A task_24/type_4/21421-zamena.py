from string import ascii_uppercase, digits

with open(r'../files/24_21421.txt') as file:
    data = file.readline()

alf = digits + ascii_uppercase

for i in alf[12:]:
    data = data.replace(i, ' ')

data = data.split()
ans = 0
for i in data:
    while i and i[0] == '0':
        i = i[1:]
    while i and i[-1] in '13579B':
        i = i[:-1]
    ans = max(ans, len(i))
print(ans)