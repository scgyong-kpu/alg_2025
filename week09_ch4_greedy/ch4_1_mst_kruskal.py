from pyvisalgo import KruskalVisualizer as Visualizer
# from pyvisalgo import PlanarVisualizer as Visualizer
import data_sample_cities as dsc

def union(u, v):
  global roots
  uroot = find_root(u)
  vroot = find_root(v)
  roots[vroot] = uroot

def find_root(u):
  if u != roots[u]:
    return find_root(roots[u])
  return roots[u]

# def find_root(u):
#   if u != roots[u]:
#     roots[u] = find_root(roots[u]) # 경로압축
#   return roots[u]

def main():
  vis.draw()
  vis.wait(1000)

  n_cities = len(cities)

  global roots
  roots = [x for x in range(n_cities)] 
  
  # sorted_edges = sorted(edges, key=lambda e: e[2])
  # print(sorted_edges)
  edges.sort(key=lambda e: e[2])
  copy = edges[:] # deep copy. copy = edge 로 하면 안 된다.
  vis.sort_edges()

  mst = []
  total_cost = 0

  while copy:
    u,v,w = copy.pop(0)
    if find_root(u) == find_root(v): continue
    print(f'find_root({u})={find_root(u)} find_root({v})={find_root(v)}')
    c1, c2 = cities[u], cities[v]
    total_cost += w
    mst.append((u, v))
    union(u, v)
    vis.append(u, v, w)    

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

