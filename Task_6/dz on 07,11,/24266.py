from turtle import *
screensize(3000, 3000)
tracer(False)
m = 10
x = 1
lt(90)
for i in range(4):
    fd(x * m)
    rt(90)
    fd(48 * m)
    rt(90)
up()
fd(27 * m)
rt(90)
fd(24 * m)
rt(90)
down()
for i in range(4):
    fd(29)
    rt(90)
    bk(18)
    rt(90)
up()
for x in range(0, 50):
    for y in range(0, 30):
        goto(x * m, y * m)
        dot(3, 'Blue')
update()
done()