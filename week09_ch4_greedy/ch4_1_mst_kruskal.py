from data_city import City, five_letter_cities
# from pyvisalgo import KruskalVisualizer as Visualizer
from pyvisalgo import PlanarVisualizer as Visualizer
import random

if __name__ == '__main__':
  vis = Visualizer('Cities')
  beg = random.randrange(100)
  end = beg + random.randrange(3, 30)
  cities = five_letter_cities[beg:end]
  vis.setup(vis.get_main_module())
  vis.draw()
  vis.end()