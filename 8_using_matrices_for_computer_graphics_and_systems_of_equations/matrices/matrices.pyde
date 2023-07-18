xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax - xmin
rangey = ymax - ymin

fmatrix = [[0,0], [1,0], [1,2], [2,2], [2,3], [1,3], [1,4], [3,4], [3,5], [0,5], [0,0]]


def setup():
    global xscl, yscl
    size(600, 600)
    
    xscl = width / rangex
    yscl = -height / rangey
    noFill()

def draw():
    global xscl, yscl
    background(255)
    translate(width/2, height/2)
    grid(xscl, yscl)
    
    strokeWeight(2)
    stroke(0)
    graph_points(fmatrix)
    
    
def graph_points(matrix):
    beginShape()
    for pt in matrix:
        vertex(pt[0]*xscl, pt[1]*yscl)
    endShape()

    
def grid(xscl, yscl):
    strokeWeight(1)
    stroke(0, 255, 255)
    
    for i in range(xmin, xmax+1):
        line(i*xscl, ymin*yscl, i*xscl, ymax*yscl)
    for i in range(ymin, ymax+1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
        
    stroke(0)
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
