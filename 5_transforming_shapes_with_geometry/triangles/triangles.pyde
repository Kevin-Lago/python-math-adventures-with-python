t = 0


def setup():
    size(600, 600)
    rectMode(CENTER)
    colorMode(HSB)


def draw():
    global t
    background(255)
    translate(width / 2, height / 2)
    rotate(radians(t))
    for i in range(90):
        stroke(4*i, 255, 255)
        rotate(radians(360 / 90))
        pushMatrix()
        translate(200, 0)
        rotate(radians(t+2*i*360/90))
        specialRightTriangle(100)
        popMatrix()
    t += 0.5
    
    
def specialRightTriangle(length):
    noFill()
    triangle(0, -length, -length * sqrt(3) / 2, length / 2, length * sqrt(3) / 2, length / 2)
