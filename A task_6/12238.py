from turtle import *
m = 10
tracer(False)

lt(90)
for i in range(2):
    fd(5 * m)
    lt(90)
    bk(13 * m)
    lt(90)
up()
bk(10 * m)
rt(90)
fd(9 * m)
lt(90)
down()
for i in range(2):
    fd(11 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()
teleport(0, 0)
rt(90)
for x in range(0, 17):
    for y in range(-10, 6):
        goto(x * m, y * m)
        dot(3, 'blue')
update()
done()