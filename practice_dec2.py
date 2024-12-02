# Rebecca Pedraza
# Dec 2

def x2_minus3x_plus4(x): # Function that returns the value of y for given x
    # Where equation is x2-3x+4
    return x**2 - 3*x + 4
print(x2_minus3x_plus4(0))

def quad(a,b,c,x): # Function that works for ax2+bx+c
    return (a * (x ** 2)) + (b * x) + c # Will return y 
print(quad(1,-3,4,0)) 

# Other way to do it
# print(quad(a = 1, b = -3, c = 4, x = 0)

import turtle

turtle.teleport(0, x2_minus3x_plus4(0))

for i in range(1, 30):
    turtle.goto(i,x2_minus3x_plus4(i))

'''  
turtle.penup()
turtle.goto(-10, 10)
turtle.pendown()
turtle.color("green")
for i in range(-10, 11):
    turtle.goto()
'''
