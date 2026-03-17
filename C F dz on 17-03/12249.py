with open(r'./files/17_12249.txt') as file:
    data = [int(i) for i in file]

ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = str(num1)[-1] == '3'
    u2 = str(num2)[-1] == '3'
    u3 = str(num3)[-1] == '3'
    if len(str(max(data))) == 5 and str(max(data))[-1] == '3':
        max_n = max(data)
        if (u1 + u2 + u3 >= 1) and (num1 + num2 + num3 <= max_n):
            ans.append(num1 + num2 + num3)
print(len(ans), max(ans))