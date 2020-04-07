import math

class Topology:

  def __init__(self, a, b):
    # Constructor- sets a and b values. 
    self.a = a
    self.b = b
  
  def addTopo(self):
    # Takes Topology object and calculates its metric.
    return (self.a**2 + self.b**2)

  def removeTopo(self):
    # Takes a Topology object and outputs its roots.
    root_a = math.sqrt(self.a)
    root_b = math.sqrt(self.b)
    return root_a, root_b 
