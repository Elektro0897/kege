with open(r'./files/17_9786.txt') as file:
    data = [int(i) for i in file]

max_25 = max(i for i in data if abs(i) % 100 == 25)
ans = []

for nums in zip(data, data[1:], data[2:]):
    k = [1 for num in nums if len(str(abs(num))) == 4]
    if sum(k) <= 2 and sum(nums) <= max_25:
        ans += [sum(nums)]
print(len(ans), max(ans))