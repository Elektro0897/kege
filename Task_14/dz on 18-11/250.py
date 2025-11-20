f = 0
for x in range(1,41):
    if bin(x)[-4:] == '1011':
        f = x
print(f)
print('ответ: 27')