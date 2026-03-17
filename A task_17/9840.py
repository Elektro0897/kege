with open(r'./files/17_9840.txt') as file:
    data = [int(i) for i in file]

max_39 = max(i for i in data if len(str(i)) == 4 and abs(i) % 100 == 39)
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = len(str(abs(num1))) == 4
    u2 = len(str(abs(num2))) == 4
    if u1 + u2 == 1 and (num1 + num2)**2 <= max_39**2:
        ans.append(num1 + num2)
print(len(ans), max(ans))