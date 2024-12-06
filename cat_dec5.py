# Rebecca Pedraza
# Dec 5

import DrawingPanel

panel = DrawingPanel.DrawingPanel(700,700)

# Cat figure
def cat_head():
    panel.fill_oval(200,200,320,320,"orange") # Head of the cat

def cat_eyes():
    panel.fill_oval(240, 240, 70, 70,"white")  
    panel.fill_oval(390, 240, 70, 70,"white")
    panel.fill_oval(270, 250, 15, 50,"black")
    panel.fill_oval(420, 250, 15, 50,"black")
    panel.set_color("black")
   
def cat_nose():
    panel.fill_polygon(330, 370, 350, 390, 310, 390, fill="pink", outline="black")

def cat_whiskers():
    panel.draw_line(300, 380, 200, 370)
    panel.draw_line(300, 390, 200, 390)
    panel.draw_line(300, 400, 200, 410)
    panel.draw_line(360, 380, 460, 370)
    panel.draw_line(360, 390, 460, 390)
    panel.draw_line(360, 400, 460, 410)
    
def cat_mouth(): 
    panel.set_color("black")
    panel.draw_line(330, 390, 310, 410)
    panel.draw_line(330, 390, 350, 410)

def cat_ears():
    panel.fill_polygon(270, 140, 320, 200, 220, 200, fill="orange", outline="black")   
    panel.fill_polygon(430, 140, 480, 200, 380, 200, fill="orange", outline="black")
    
# Draw cat
cat_head()
cat_eyes()
cat_nose()
cat_whiskers()
cat_mouth()
cat_ears()
