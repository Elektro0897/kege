from turtle import *
screensize(3000, 3000)
m = 10
tracer(False)
lt(90)
for i in range(2):
    fd(23 * m)
    lt(90)
    bk(27 * m)
    lt(90)
up()
bk(5 * m)
rt(90)
fd(11 * m)
lt(90)
down()
for i in range(2):
    fd(26 * m)
    rt(90)
    fd(32 * m)
    rt(90)
up()
for x in range(0, 50):
    for y in range(-10, 30):
        goto(x * m, y * m)
        dot(3, 'blue')
update()
done()