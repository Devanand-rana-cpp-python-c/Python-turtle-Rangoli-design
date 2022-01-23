import turtle
t=turtle.Turtle()
screen=t.getscreen()
col="salmon"
def flower():
    t.fillcolor(col)
    t.begin_fill() 
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(135)
    t.forward(283)  
    t.end_fill() 
def flower2():
    col1="green"
    t.fillcolor(col1)
    t.begin_fill() 
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(135)
    t.forward(283)   # 283?.... C = ((200**2+200*2)+0.5**2) 
    t.end_fill()
def text():
    t.setpos(-150,0)
    t.color="yellow"
    t.write("Hello Dev \U0001F600",font=("algerian",30,"italic"))  
    
for i in range(4):
    flower()
    flower2()

print(i)
screen.bgcolor("cyan")
text()
    
screen.exitonclick()

