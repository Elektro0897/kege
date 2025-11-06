from turtle import *
screensize(3000, 3000)
tracer(False)
m = 10
lt(90)
rt(270)
for i in range(2):
    fd(8 * m)
    rt(120)
rt(120)
for i in range(2):
    rt(120)
    fd(3 * m)
    rt(240)
rt(240)
for i in range(2):
    fd(14 * m)
    rt(120)
up()
for x in range(-10, 10):
    for y in range(0, 15):
        goto(x * m, y * m)
        dot(3, 'Blue')
up()
goto(0, 0)
down()
goto(-100 * m, 0)
goto(100 * m, 0)
up()
goto(0, 0)
down()
goto(0, -100 * m)
goto(0, 100 * m)
update()
done()
print("S = h * a")
print("ответ: 195")