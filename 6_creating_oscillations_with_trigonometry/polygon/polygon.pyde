def setup():
    size(600, 600)
    
    
def draw():
    translate(width / 2, height / 2)
    polygon(6, 100)
    

def polygon(sides, sz):
    beginShape()
    step = radians(360 / sides)
    for i in range(sides):
        vertex(sz*cos(i*step),sz*sin(i*step))
    endShape()


def basic_shape():
    beginShape()
    vertex(100, 100)
    vertex(100, 200)
    vertex(200, 200)
    vertex(200, 100)
    vertex(150, 50)
    endShape(CLOSE)
