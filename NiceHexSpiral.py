#NiceHexSpiral.py
import turtle   
colors=['red', 'orange', 'yellow',
        'green', 'blue', 'purple']
t=turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)        
    t.left(59)
