r1 = 300.0
r2 = 175.0
r3 = 5.0
x1 = 0
y1 = 0
t = 0
points = []
prop = 0.9


def setup():
    size(600, 600)
    
    
def draw():
    global r1, r2, r3, x1, y1, t, prop, points
    translate(width/2, height/2)
    background(255)
    noFill()
    stroke(0)
    ellipse(x1, y1, 2*r1, 2*r1)
    
    x2 = (r1 - r2)*cos(t)
    y2 = (r1 - r2)*sin(t)
    ellipse(x2, y2, 2*r2, 2*r2)
    
    x3 = x2+prop*(r2 - r3)*cos(-((r1-r2)/r2)*t)
    y3 = y2+prop*(r2 - r3)*sin(-((r1-r2)/r2)*t)
    
    fill(255, 0, 0)
    ellipse(x3, y3, 2*r3, 2*r3)
    points = [[x3, y3]] + points[:2000]
    
    for i, p in enumerate(points):
        if i < len(points) - 1:
            stroke(255, 0, 0)
            line(p[0], p[1], points[i+1][0], points[i+1][1])
    
    t += 0.05
