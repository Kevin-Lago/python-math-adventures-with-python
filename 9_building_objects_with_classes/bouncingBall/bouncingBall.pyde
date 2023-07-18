balls = []


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xvel = random(-2, 2)
        self.yvel = random(-2, 2)
        self.col = color(random(255),
                         random(255),
                         random(255))
        self.size = random(5, 50)

    def update(self):
        self.x += self.xvel
        self.y += self.yvel
        
        if self.x > width-(self.size/2) or self.x < self.size/2:
            self.xvel = -self.xvel
        if self.y > height-(self.size/2) or self.y < self.size/2:
            self.yvel = -self.yvel
            
        fill(self.col)
        ellipse(self.x, self.y, self.size, self.size)


def setup():
    size(600, 600)
    
    for i in range(30):
        balls.append(Ball(random(width), random(height)))
    
    
def draw():
    background(0)
    for ball in balls:
        ball.update()
