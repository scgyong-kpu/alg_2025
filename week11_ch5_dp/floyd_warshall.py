# Shortest Path - Floyd Warshall
from city import City, five_letter_cities
import two_d_visualizer as vis
import random
from math import sqrt

class Floyd:
  def __init__(self):
    self.cities = [
      City("Quiff", 525, 248, 0),
      City("Wrote", 1, 260, 1),
      City("Thong", 190, 385, 2),
      City("Melon", 527, 416, 3),
      City("React", 296, 659, 4),
      City("Rabbi", 6, 758, 5),
      City("Auger", 442, 866, 6),
    ]
    self.n_cities = len(self.cities)
    self.input = {
      0: { 1:662, 2:613, 3:162, },
      1: { 0:272, 2:240, 5:278, },
      2: { 1:174, 0:413, 4:167, },
      3: { 0:172, 2:300, 6:649, },
      4: { 5:219, 6:272, },
      5: { 1:374, 2:311, 4:223, 6:539, },
      6: { 5:436, 4:314, 3:586, },
    }
    self.INF = float('inf')
    self.dgraph = [
      [ self.INF for _ in range(self.n_cities) 
      ] for _ in range(self.n_cities) 
    ]
    self.dirs = [
      [ -1 for _ in range(self.n_cities) 
      ] for _ in range(self.n_cities)
    ]


  def start(self):
    pass

    vis.floyd_update()



def distance(c1, c2):
  dx, dy = c1.x - c2.x, c1.y - c2.y
  return sqrt(dx ** 2 + dy ** 2)

floyd = Floyd()

if __name__ == '__main__':
  random.seed('hello')
  vis.init('Shortest Path - Floyd Warshall')
  # vis.speed = 200
  vis.floyd_init(floyd)
  floyd.start()
  vis.end()
