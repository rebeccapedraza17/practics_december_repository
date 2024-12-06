# Rebecca Pedraza
# Dec 6

import DrawingPanel

panel = DrawingPanel.DrawingPanel(800,600)

def draw_sun():
    panel.fill_oval(90, 90, 100, 100,"orange")
draw_sun()

def draw_background():
    panel.fill_rect(0, 450, 800, 500, "green")
draw_background()
    
def draw_car():
    panel.fill_rect(100, 400, 40, 40, "red")
    panel.fill_rect(140, 400, 10, 10, "red")
    panel.fill_rect(90, 400, 10, 10, "red")
    panel.fill_oval(75, 425, 25, 25, "black")
    panel.fill_oval(140, 425, 25, 25, "black")
draw_car()


def draw_clouds():
    panel.fill_oval(550, 90, 100, 100, "blue")
    panel.fill_oval(500, 80, 100, 100, "blue")
    panel.fill_oval(460, 90, 100, 100, "blue")
draw_clouds()

def animate_car():
    for i in range(0, 800, 5):
        draw_car(i)
        time.sleep(10000)
animate_car()

def draw_cactus():
    panel.fill_(
