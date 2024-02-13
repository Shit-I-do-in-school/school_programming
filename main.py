import turtle
import random
import math

turtle.shape("turtle")
turtle.color('red')

distans = random.randint(-15, 15)
vinkel = random.randint(-180, 180)

x = 1
while True:
  turtle.forward(random.randint(-5, 5))
  turtle.left(random.randint(-5, 5))
  x += 1
  print(x)