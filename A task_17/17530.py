with open(r'./files/17_17530.txt') as file:
    data = [int(i) for i in file]

min_n = min(data)
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = num1 % 55 == min_n
    u2 = num2 % 55 == min_n
    if u1 + u2 >= 1:
        ans.append(num1 + num2)
print(len(ans), min(ans))