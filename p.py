import math

class circle:
  def __init__(self,r):
    self.r = r

  def area(self):
    return math.pi * (self.r ** 2)

  def circumference(self):
    return 2 * math.pi * self.r
    
radius=float(input("Enter radius "))
circle1=circle(radius)
print("Arear is",circle1.area())
print("Paremeter is",circle1.paremeter())
