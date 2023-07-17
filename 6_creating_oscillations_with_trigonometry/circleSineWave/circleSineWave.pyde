r1 = 100
r2 = 10
t = 0
circleList = []


def setup():
    size(600, 600)
    
    
def draw():
    global r1, r2, t, circleList
    
    background(200)
    translate(width / 4, height / 2)
    noFill()
    stroke(0)
    ellipse(0, 0, 2*r1, 2*r1)
    
    fill(255, 0, 0)
    y = r1*sin(t)
    x = r1*cos(t)
    
    circleList = [y] + circleList[:249]
    ellipse(x, y, r2, r2)
    
    stroke(0, 255, 0)
    line(x, y, 200, y)
    fill(0, 255, 0)
    ellipse(200, y, 10, 10)
    
    for i, c in enumerate(circleList):
        ellipse(200 + i, c, 5, 5)
    
    t += .05
