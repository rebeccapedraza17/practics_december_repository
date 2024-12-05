# Rebecca Pedraza
# Dec 3

import DrawingPanel

panel = DrawingPanel.DrawingPanel(700,700)


# Examples to do in Drawing Panel
'''
panel.draw_line(x1,y1,x2,y2)
panel.draw_rect(x1,y1,w,h)
panel.draw_oval(x1,y1,w,h)
panel.fill_rect(x,y,w,h)
panel.fill_oval(x,y,w,h)
panel.set_color("colorname")
'''
'''
# Rectangle
panel.draw_rect(50,60,59,69)
panel.set_color("orange")
panel.fill_rect(50,60,59,69)
'''

# Draw 5 circles in a corner, each circle increases at constant value
panel.draw_oval(100,100,30,30)
panel.draw_oval(95,95,60,60)
panel.draw_oval(90,90,90,90)
panel.draw_oval(85,85,120,120)
panel.draw_oval(80,80,150,150)

# Draw 10 stacked rectangles 

# Blue rectangle at 100,100, width 100 & height 50, 5 pixel balckoutline


# Draw a red ball of size 20, moves diagonally, from left to right (bottom)



