# Rebecca Pedraza
# Dec 5

import DrawingPanel

panel = DrawingPanel.DrawingPanel(700,700)

ball = panel.create_oval(10, 10, 20, 20, fill='red')

while True:
    ball.move(1, 1)
    panel.update()
    panel.sleep(10)
print 
