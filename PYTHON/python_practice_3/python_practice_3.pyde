def setup():
    size(800,800)
    smooth()
    
    global c, d
    c = color(random(255), random(255), random(255))
    d = color(random(255), random(255), random(255))

def draw():
    global c, d
    background(255)
    stroke(0)
    noFill()
    constantFactor = 1.3
    circleSize = 25
    
    for i in range(0,17):
        p = lerpColor(c, d, 1.0 * 1/width)
        stroke(p)
        # line(x, 0, x, height)
        
        strokeWeight(circleSize/25)
        ellipse(width/2, height, circleSize, circleSize)
        circleSize = circleSize * constantFactor
        
def mousePressed():
    global c, d
    c = color(random(255), random(255), random(255))
    d = color(random(255), random(255), random(255))
