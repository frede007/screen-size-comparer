from turtle import *
from math import sqrt

lt_winp = int(input("Left screen width in pixels: "))
lt_hinp = int(input("Left screen height in pixels: "))
lt_d = float(input("Left screen diagonal in inches: "))
lt_split = (input("Split left screen? ")).lower()

rt_winp = int(input("Right screen width in pixels: "))
rt_hinp = int(input("Right screen height in pixels: "))
rt_d = float(input("Right screen diagonal in inches: "))
rt_split = (input("Split right screen? ")).lower()

lt_h = round((lt_hinp * lt_d)  / (sqrt((lt_winp ** 2) + (lt_hinp ** 2))), 1)
lt_w = round((lt_winp * lt_d) / (sqrt((lt_winp ** 2) + (lt_hinp ** 2))), 1)
rt_h = round((rt_hinp * rt_d)  / (sqrt((rt_winp ** 2) + (rt_hinp ** 2))), 1)
rt_w = round((rt_winp * rt_d) / (sqrt((rt_winp ** 2) + (rt_hinp ** 2))), 1)

lt_h_in = lt_h
lt_w_in = lt_w
rt_h_in = rt_h
rt_w_in = rt_w

multiplier = 16
lt_h *= multiplier
lt_w *= multiplier
rt_h *= multiplier
rt_w *= multiplier
lt_h = int(lt_h)
lt_w = int(lt_w)
rt_h = int(rt_h)
rt_w = int(rt_w)

lt_ppi = round(((sqrt((lt_winp ** 2) + (lt_hinp ** 2))) / lt_d), 2)
rt_ppi = round(((sqrt((rt_winp ** 2) + (rt_hinp ** 2))) / rt_d), 2)

print(f"""  
    Left screen:
    Width: {lt_w_in} in, {lt_winp} pix
    Height: {lt_h_in} in, {lt_hinp} pix
    PPI: {lt_ppi} PPI

    Right screen:
    Width: {rt_w_in} in, {rt_winp} pix
    Height: {rt_h_in} in, {rt_hinp} pix
    PPI: {rt_ppi} PPI
    """)

ht()
up()
setx(-600)
sety(200)
pd()

forward(lt_w)
right(90)
forward(lt_h)
right(90)
forward(lt_w)
right(90)
forward(lt_h)

right(90)
up()
forward(lt_w + 30)
right(90)
forward(lt_h - rt_h)
left(90)
pd()

forward(rt_w)
right(90)
forward(rt_h)
right(90)
forward(rt_w)
right(90)
forward(rt_h)

if rt_split == 'yes' and lt_split == 'no':
    right(90)
    forward(rt_w / 2)
    right(90)
    forward(rt_h)
    done()
elif rt_split == 'yes' and lt_split == 'yes':
    right(90)
    forward(rt_w / 2)
    right(90)
    forward(rt_h)
    up()
    right(90)
    forward((rt_w / 2) + 30 + (lt_w / 2))
    right(90)
    pd()
    forward(lt_h)
    done()
elif lt_split == 'yes' and rt_split == 'no':
    up()
    left(90)
    forward(30 + (lt_w / 2))
    right(90)
    forward(lt_h - rt_h)
    pd()
    right(180)
    forward(lt_h)
    done()
else:
    done()

