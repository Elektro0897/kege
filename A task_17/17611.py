with open(r'./files/17_17611.txt') as file:
    data = [int(i) for i in file]

max_7_4 = max(i for i in data if str(i)[-1] == '7' and len(str(abs(i))) == 4)
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = len(str(abs(num1))) == 4 and str(num1)[-1] == '7'
    u2 = len(str(abs(num2))) == 4 and str(num2)[-1] == '7'
    u3 = len(str(abs(num3))) == 4 and str(num3)[-1] == '7'
    u4 = num1 + num2 + num3 > max_7_4
    if u1 + u2 + u3 >= 2 and u4:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))
# 3 57250