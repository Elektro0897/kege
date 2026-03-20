with open(r'./files/17_18617.txt') as file:
    data = [int(i) for i in file]

max_n = max(i for i in data)
min_n = min(i for i in data)
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = num1 % 3 == max_n % 3
    u2 = num2 % 3 == max_n % 3
    f1 = num1 % 7 == min_n % 7
    f2 = num2 % 7 == min_n % 7
    if u1 + u2 >= 1 and f1 + f2 >= 1:
        ans.append(num1 + num2)
print(len(ans), max(ans))