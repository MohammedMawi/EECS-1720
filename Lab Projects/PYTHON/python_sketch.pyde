def setup():
    size(800, 600)

def draw():
    if  mousePressed:
        fill(0,255,0)
    else:
        fill(255,0,0)
    ellipse(mouseY, mouseX, 120, 120)