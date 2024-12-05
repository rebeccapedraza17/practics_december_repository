# Rebecca Pedraza
# Dec 5

import DrawingPanel

panel = DrawingPanel.DrawingPanel(700,700)

# Cat figure
def cat_head():
    panel.fill_oval(200,200,300,300,"orange") # Head of the cat

def cat_eyes():
    # Left eye 
    panel.fill_oval(240, 240, 70, 70,"white")  
    # Right eye 
    panel.fill_oval(390, 240, 70, 70,"white")
    # Left pupil 
    panel.fill_oval(255, 255, 30, 30,"black")
    # Right pupil 
    panel.fill_oval(405, 255, 30, 30,"black")
   
def cat_nose():
    panel.fill_oval(315,330,30,30,"pink")

def cat_whiskers():
    # Left side
    panel.draw_line(220, 330, 150, 340)
    panel.draw_line(220, 340, 150, 350)
    panel.draw_line(220, 350, 150, 360)
    # Right side
    panel.draw_line(440, 330, 510, 340)
    panel.draw_line(440, 340, 510, 350)
    panel.draw_line(440, 350, 510, 360)
    
def cat_mouth():
    # Left mouth 
    panel.set_color("black")
    panel.draw_line(330, 340, 270, 380)
    # Right mouth 
    panel.draw_line(330, 340, 390, 380)

def cat_ears():
    # Left ear
    panel.fill_polygon(200, 170, 240, 100,"orange")
    # Right ear 
    panel.fill_polygon(500, 460, 460, 170,"orange")

# Draw cat
cat_head()
cat_eyes()
cat_nose()
cat_whiskers()
cat_mouth()
cat_ears()
