from string import printable as alf
# for x in alf[:]:
#     for y in alf[:]:
#         num1 = int(f'73{x}1{y}', 67)
#         num2 = int(f'49{y}6', x)
#         num = num1 + num2
#         if num:
#             print(num)
res = set()
for x in range(10, 67):
    for y in range(x):
        num1 = 7*67**4 + 3*67**3 + x*67**2 + 1*67**1 + y*67**0
        num2 = 4*x**3 + 9*x**2 + y*x**1 + 6*x**0
        num = num1 + num2
        res.add(num)
print(len(set(res)))