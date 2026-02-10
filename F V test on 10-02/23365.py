from turtle import *
screensize(3000, 3000)
tracer(False)
m = 10
lt(90)
for i in range(3):
    fd(39*m)
    rt(90)
    fd(48*m)
    rt(90)
up()
fd(27*m)
rt(90)
fd(24*m)
lt(90)
down()
for i in range(3):
    fd(29*m)
    rt(90)
    bk(18*m)
    rt(90)
up()
for x in range(24, 43):
    for y in range(0, 13):
        goto(x * m, y * m)
        dot(3, 'blue')
update()
done()