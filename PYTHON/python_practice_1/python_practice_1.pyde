def setup():
    size(800,800)
    smooth()

def draw():
    background(255)
    stroke(0)
    noFill()
    constantFactor = 1.3
    circleSize = 25
    
    for i in range(0,17):
        strokeWeight(circleSize/25)
        ellipse(width/2, height, circleSize, circleSize)
        circleSize = circleSize * constantFactor
