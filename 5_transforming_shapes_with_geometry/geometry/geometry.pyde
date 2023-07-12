t = 0


def setup():
    rectMode(CENTER)
    size(600, 600)


def draw():
    global t
    translate(width/2, height/2)
    rotate(radians(t))
    for i in range(12):
        pushMatrix()
        translate(200, 0)
        rotate(radians(5*t))
        rect(0, 0, 50, 50)
        popMatrix()
        rotate(radians(360 / 12))
    t+=1
