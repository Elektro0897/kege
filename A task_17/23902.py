with open(r'.\files\17_23902.txt') as file:
    data = [int(i) for i in file]

ans = []
for nums in zip(data, data[1:], data[2:]):
    u1 = sum(str(i)[0] == str(i)[-1] for i in nums) == 1
    u2 = sum(1000 <= i <= 9999 and str(i)[1] == '2' for i in nums) == 2
    if u1 and u2:
        ans.append(max(nums))
print(len(ans), sum(ans))