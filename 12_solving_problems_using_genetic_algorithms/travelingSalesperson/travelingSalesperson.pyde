import random


class City:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number
        
    def display(self):
        fill(0, 255, 255)
        ellipse(self.x, self.y, 10, 10)
        textSize(20)
        text(self.number, self.x-10, self.y-10)
        noFill()
        
        
class Route:
    def __init__(self):
        self.distance = 0
        self.cityNums = random.sample(list(range(N_CITIES)), N_CITIES)
        
    def display(self):
        strokeWeight(3)
        stroke(255, 0, 255)
        beginShape()
        for i in self.cityNums:
            vertex(cities[i].x, cities[i].y)
            cities[i].display()
        endShape(CLOSE)
        
    def calcLength(self):
        self.distance = 0
        for i, number in enumerate(self.cityNums):
            self.distance += dist(cities[number].x, cities[number].y, cities[self.cityNums[i-1]].x, cities[self.cityNums[i-1]].y)
        return self.distance
    
    def mutateN(self, number):
        indices = random.sample(list(range(N_CITIES)), number)
        child = Route()
        child.cityNums = self.cityNums[::]
        
        for i in range(number-1):
            child.cityNums[indices[i]], child.cityNums[indices[(i+1)%number]] = child.cityNums[indices[(i+1)%number]], child.cityNums[indices[i]]
    
        return child
    
    def crossover(self, partner):
        child = Route()
        index = random.randint(1, N_CITIES - 2)
        child.cityNums = self.cityNums[:index]
        if random.random() < 0.5:
            child.cityNums = child.cityNums[::-1]
        
        notinslice = [x for x in partner.cityNums if x not in child.cityNums]
        child.cityNums += notinslice
        return child
        

cities = [
          # City(100, 100, 0),
          # City(300, 100, 1),
          # City(300, 300, 2),
          # City(100, 300, 3)
          ]
N_CITIES = 20
random_improvements = 0
mutated_improvements = 0
population = []
POP_N = 1000


def setup():
    global best, record_distance, first, population
    size(600, 600)
    background(0)
    
    for i in range(N_CITIES):
        cities.append(City(random.randint(50, width-50), random.randint(50, height-50), i))
        
        
    for i in range(POP_N):
        population.append(Route())
        
    best = Route()
    record_distance = best.calcLength()
    first = record_distance
    
    
def draw():
    global best, record_distance, population
    background(0)
    best.display()
    println(record_distance)
    population.sort(key=Route.calcLength)
    population = population[:POP_N]
    length1 = population[0].calcLength()
    
    if length1 < record_distance:
        record_distance = length1
        best = population[0]
        
    for i in range(POP_N):
        parentA, parentB = random.sample(population, 2)
        child = parentA.crossover(parentB)
        population.append(child)
        
    for i in range(3, 25):
        if i < N_CITIES:
            new = best.mutateN(i)
            population.append(new)
            
    for i in range(3, 25):
        if i < N_CITIES:
            new = random.choice(population)
            new = new.mutateN(i)
            population.append(new)
