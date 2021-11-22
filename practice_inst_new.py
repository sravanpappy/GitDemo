import turtle

col=('yellow','red','green','orange','blue','white')

t=turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(10000)
for i in range (500):
     t.color(col[i%6])
     t.forward(i*1)
     t.left(550)
     t.width(2)

#max({3,2,1})


a="pythonhub"
b="pythonHub"
print(a==b)
aa="A"
ab="a"
print(aa < ab)
