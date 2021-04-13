import turtle as t


n = 50
t.bgcolor("black")
t.color("red")
t.speed(0)
for x in range(n):
  t.circle(80)
  t.left(360/n)
  
n = 80
t.bgcolor("black")
t.color("blue")
t.speed(0)
for x in range(n):
  t.circle(80)
  t.left(360/n)
  
angle = 89
t.bgcolor("black")
t.color("black")
t.speed(0)
for x in range(200):
  t.forward(x)
  r.left(angle)
