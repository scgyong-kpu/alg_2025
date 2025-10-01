from pyvisalgo import SelectionVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

import ch3_2_quick_sort as qs

def main():
  qs.array = array
  qs.vis = vis
  print('before:', array)
  count = len(array)
  vis.push(0, count-1, n_th)
  pi = qs.partition(0, count-1)
  vis.set_pivot(pi)

if __name__ == '__main__':
  seed('SelectionSeed')
  vis = Visualizer('Selection')
  while True:
    count = randint(20, 40)
    array = [ randint(1, 99) for _ in range(count) ]
    shuffle(array)
    n_th = randint(1, count)
    # array=[4,8,10,2,1,3]
    vis.setup(vis.get_main_module())
    main()
    vis.draw()
    again = vis.end()
    if not again: break
