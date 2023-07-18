from random import choice


WHITE = color(255)
BROWN = color(102, 51, 0)
RED = color(255, 0, 0)
GREEN = color(0, 102, 0)
YELLOW = color(255, 255, 0)
PURPLE = color(102, 0, 204)

COLORS = [WHITE, RED, YELLOW, PURPLE]


class Sheep:
    def __init__(self, x, y, col):
        self.x = x
        self.y = y
        self.sz = 10
        self.energy = 20
        self.col = col
        self.age = 30
        
    def update(self):
        self.energy -= 1
        if self.energy <= 0:
            sheepList.remove(self)
            
        self.age -= 1
        if self.age <= 0:
            sheepList.remove(self)
            
        self.x += random(-self.sz, self.sz)
        self.y += random(-self.sz, self.sz)
        
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
            
        xscl = int(self.x/patchSize)
        yscl = int(self.y/patchSize)
        
        grass = grassList[xscl * rows_of_grass + yscl]
        
        if not grass.eaten:
            self.energy += grass.energy
            grass.eaten = True
            
        if self.energy >= 50:
            self.energy -= 30
            sheepList.append(Sheep(self.x, self.y, self.col))
        
        fill(self.col)
        ellipse(self.x, self.y, self.sz, self.sz)
        
        
class Grass:
    def __init__(self, x, y, sz):
        self.x = x
        self.y = y
        self.energy = 9
        self.eaten = False
        self.sz = sz
        
    def update(self):
        if self.eaten:
            if random(100) < 5:
                self.eaten = False
            else:
                fill(BROWN)
        else:
            fill(GREEN)
        rect(self.x, self.y, self.sz, self.sz)
        

sheepList = []
grassList = []
patchSize = 10
        
        
def setup():
    global patchSize, rows_of_grass
    rows_of_grass = height/patchSize
    size(600, 600)
    noStroke()
    
    for i in range(3):
        sheepList.append(Sheep(random(width), random(height), choice(COLORS)))
        
    for x in range(0, width, patchSize):
        for y in range(0, height, patchSize):
            grassList.append(Grass(x, y, patchSize))
    
    
def draw():
    background(255)
    for grass in grassList:
        grass.update()
    for sheep in sheepList:
        sheep.update()
