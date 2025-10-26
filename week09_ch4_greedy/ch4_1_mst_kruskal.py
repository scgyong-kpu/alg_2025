# from pyvisalgo import KruskalVisualizer as Visualizer
from pyvisalgo import PlanarVisualizer as Visualizer
import data_sample_cities as dsc

if __name__ == '__main__':
  vis = Visualizer('Cities')
  cities, edges = dsc.cities, dsc.edges
  vis.setup(vis.get_main_module())
  vis.draw()
  vis.end()