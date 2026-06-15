with open(r'./files/17_28938.txt') as file:
    data = [int(i) for i in file]

max_28 = max(i for i in data if str(i)[-2:] == '28')
ans = []
for nums in zip(data, data[1:], data[2:]):
    u1 = 0
    for num in nums:
        if len(str(abs(num))) == 3:
            u1 += 1
    u2 = 0 < sum(nums) / 3 < max_28
    if u1 >= 1 and u2:
        ans.append(sum(nums))
print(len(ans), max(ans))