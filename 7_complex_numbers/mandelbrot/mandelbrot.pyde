xmin = -2
xmax = 2

ymin = -2
ymax = 2

rangex = xmax - xmin
rangey = ymax - ymin


def setup():
    global xscl, yscl
    size(600, 600)
    colorMode(HSB)
    noStroke()
    
    xscl = width/float(rangex)
    yscl = height/float(rangey)
    println("stop")
    
    
def draw():
    println("stop")
    translate(width/2, height/2)
    x = xmin
    while x < xmax:
        y = ymin
        
        while y < ymax:
            z = [x, y]
            c = [-0.8, 0.156]
            
            col = mandelbrot(z, 100)
            
            if col == 100:
                fill(0)
            else:
                fill(3*col, 255, 255)
                
            rect(x*xscl, y*yscl, 1, 1)
            y += 0.01
        x += 0.01
    
    
def c_add(a, b):
    return [a[0]+b[0], a[1]+b[1]]


def c_mult(u, v):
    return [u[0]*v[0]-u[1]*v[1], u[1]*v[0]+u[0]*v[1]]


def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)
    

def mandelbrot(z, num):
    count = 0
    z1 = z

    while count <= num:
        if magnitude(z1) > 2.0:
            return count

        z1 = c_add(c_mult(z1, z1), z)
        count += 1

    return num
