from string import printable
with open(r'./files/24_26551.txt') as file:
    data = file.readline()

for i in set(data):
    if i not in printable[:14]:
        data = data.replace(i, ' ')

data = data.split()
ans = 0
for line in data:
    line = line.rstrip('13579BD')
    line = line.lstrip('0')
    ans = max(ans, len(line))
print(ans)
###############################################
from re import finditer
with open(r'./files/24_26551.txt') as file:
    data = file.readline()

pattern = r'[1-9ABCD][0-9ABCD]*[02468AC]'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=lambda x: int(x, 14))))