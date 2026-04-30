with open(r'./files/17_11236.txt') as file:
    data = [int(i) for i in file]

min_2 = min(i for i in data if len(str(abs(i))) == 2)
max_4 = max(i for i in data if str(i)[-1] == '1' and len(str(abs(i))) == 4)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = num1 > min_2**2
    u2 = num2 > min_2 ** 2
    u3 = num3 > min_2 ** 2
    u4 = abs(num1) * abs(num2) * abs(num3) % max_4 == 0
    if u1 + u2 + u3 == 2 and u4:
        ans.append(sum(map(abs, (num1, num2, num3))))
print(len(ans), max(ans))
