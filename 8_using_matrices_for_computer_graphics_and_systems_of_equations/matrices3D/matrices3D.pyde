xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax - xmin
rangey = ymax - ymin

fmatrix = [[0,0], [1,0], [1,2], [2,2], [2,3], [1,3], [1,4], [3,4], [3,5], [0,5], [0,0]]
rotation_matrix = [[0,-1], [1,0]]
reflection_matrix = [[1,0], [0,-1]]
# tm2 = [[0,-1], [-1,0]]
# tm2 = [[-1,1], [1,1]]


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
    
    ang = map(mouseX,0,width,0,TWO_PI)
    rotation_matrix = [[cos(ang), -sin(ang)], [sin(ang), cos(ang)]]
    
    strokeWeight(2)
    stroke(0)
    graph_points(fmatrix)

    transformed_matrix = transpose(multiply_matrices(rotation_matrix, transpose(fmatrix)))
    stroke(255, 0, 0)
    graph_points(transformed_matrix)
    
    
def transpose(a):
    output = []
    m = len(a)
    n = len(a[0])
    
    for i in range(n):
        output.append([])
        for j in range(m):
            output[i].append(a[j][i])

    return output
    
    
def multiply_matrices(a, b):
    m = len(a)
    n = len(b[0])
    new_matrix = []

    for i in range(m):
        row = []
        for j in range(n):
            sum1 = 0
            for k in range(len(b)):
                sum1 += a[i][k]*b[k][j]
            row.append(sum1)
        new_matrix.append(row)
    return new_matrix
    
    
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
