import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point({self.x}, {self.y})")
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Example 
point1 = Point(3, 4)
point2 = Point(6, 8)
point1.show()
point1.move(1, 1)
point1.show()
print(point1.dist(point2))