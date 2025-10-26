from pyvisalgo import KruskalVisualizer as Visualizer
# from pyvisalgo import PlanarVisualizer as Visualizer
import data_sample_cities as dsc

def main():
  # sorted_edges = sorted(edges, key=lambda e: e[2])
  # print(sorted_edges)
  vis.draw()
  vis.wait(1000)
  edges.sort(key=lambda e: e[2])
  vis.sort_edges()
  mst = []

if __name__ == '__main__':
  vis = Visualizer('MST - Kruskal')
  while True:
    cities, edges = dsc.cities, dsc.edges
    vis.setup(vis.get_main_module())
    main()
    again = vis.end()
    if not again: break
    if vis.restart_lshift:
      dsc.next()
    elif vis.restart_rshift:
      dsc.random()

