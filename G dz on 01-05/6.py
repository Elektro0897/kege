from turtle import *
screensize(3000, 3000)
tracer(False)
n = 10
lt(90)
rt(45)
for i in range(3):
    rt(45)
    fd(10*n)
    rt(45)
rt(315)
fd(10*n)
rt(90)
fd(20*n)
rt(90)
for i in range(2):
    fd(10*n)
    rt(90)
up()
for x in range(-10, 11):
    for y in range(-10, 11):
        goto(x*n, y*n)
        dot(3, 'red')
update()
done()
print(9 * 9 * 3 + 18)
#261