from turtle import *
screensize(3000, 3000)
tracer(False)
m = 20
lt(90)
for i in range(13):
    fd(13*m)
    rt(90)
    fd(5*m)
up()
rt(90)
fd(7*m)
lt(90)
fd(10*m)
down()
for i in range(23):
    fd(8*m)
    lt(90)
    fd(11*m)
    lt(90)
up()
for x in range(15, 19):
    for y in range(6, 14):
        goto(x*m, y*m)
        dot(3, 'blue')
update()
done()
print('ответ:',19*14+9*12-8*4)
