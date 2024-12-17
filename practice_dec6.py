# Rebecca Pedraza
# Dec
# Animate car

import DrawingPanel
import time

panel = DrawingPanel.DrawingPanel(800, 600)

def draw_background():
    panel.fill_rect(0, 450, 800, 500, "green")  
    panel.fill_rect(0, 0, 800, 450, "skyblue")  
draw_background()

def draw_sun():
    panel.fill_oval(90, 90, 100, 100, "dark orange")
draw_sun()

def draw_clouds():
    panel.fill_oval(550, 90, 100, 100, "light blue")
    panel.fill_oval(500, 80, 100, 100, "light blue")
    panel.fill_oval(460, 90, 100, 100, "light blue")
draw_clouds()

def draw_tree():
    panel.fill_rect(600, 410, 20, 40, "dark green")
    panel.fill_rect(590, 390, 20, 30, "dark green")
    panel.fill_rect(610, 390, 20, 30, "dark green")
draw_tree()

def draw_car(x):
    panel.fill_rect(100, 400, 40, 40, "red")
    panel.fill_rect(140, 400, 10, 10, "red")
    panel.fill_rect(90, 400, 10, 10, "red")
    panel.fill_oval(75, 425, 25, 25, "black")
    panel.fill_oval(140, 425, 25, 25, "black")

    panel.fill_rect(x, 400, 40, 40, "red")
    panel.fill_rect(x + 40, 400, 10, 10, "red")
    panel.fill_rect(x - 10, 400, 10, 10, "red")
    panel.fill_oval(x - 25, 425, 25, 25, "black")
    panel.fill_oval(x + 40, 425, 25, 25, "black")    
draw_car()

def animate_car():
    for i in range(100):
        draw_car(i * 5)  
        time.sleep(0.05) 
animate_car()  
