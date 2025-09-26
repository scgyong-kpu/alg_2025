# from data_unsorted import numbers
# from data_unsorted_a_lot import numbers
from pyvisalgo import QuickSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
  print('before:', array)
  count = len(array)

  vis.push(0, count-1)
  partition(0, count-1)

  print('after :', array)

def partition(left, right):

  pi = left               # pi = Pivot Index
  pivot = array[pi]       # pivot = Pivot Value

  p, q = left, right + 1  # 후보선수들 출전준비

  while True:             # p < q 인 동안 하게 된다. 하지만 중간에 break 하므로 while True 를 쓰자
    while True:           # 왼쪽에서 pivot 보다 큰 값을 찾을때까지
      p += 1
      vis.set_p(p)
      if q < p: break
      if p <= right: vis.compare(pi, p)
      if p > right or array[p] > pivot: break 
      # 왼쪽에서 pivot 보다 큰 값을 찾았다

      if p <= right: vis.set_left(p)

    while True:           # 오른쪽에서 pivot 보다 작은 값을 찾을때까지
      q -= 1
      vis.set_q(q)
      if q < p: break
      if q >= left: vis.compare(pi, q)
      if q < left or array[q] < pivot: break
      # 오른쪽에서 pivot 보다 작은 값을 찾았다

      if q >= left: vis.set_right(q)

    if p >= q: break      # p 와 q 가 만날때까지 계속 진행한다
                          # 즉, p >= q 라면, 교환할 값이 없다는 뜻이다

    vis.set_left(p)
    vis.set_right(q)

    vis.swap(p, q)
    array[p], array[q] = array[q], array[p] 
    # 이제 p 이하에는 pivot 보다 작은 값만, q 이상에는 pivot 보다 큰 값만 있다


  # 이 코드는 partition() 함수의 Loop 를 모두 빠져 나온 후에 실행되는 영역이다
  # pivot 값의 위치를 확정시킨다
  # pivot 값은 왼쪽 그룹 중에 가장 큰 값이므로 q 위치로 옮긴다
  # left 가 q 와 같다면 pivot 보다 작은것이 하나도 없다는 뜻이므로 옮길 필요가 없다
  if left != q:
    vis.swap(left, q, True)
    array[left], array[q] = array[q], array[left]

if __name__ == '__main__':
  seed('Hello')
  vis = Visualizer('Quick Sort')
  while True:
    count = randint(20, 40)
    array = [ randint(1, 99) for _ in range(count) ]
    vis.setup(vis.get_main_module())
    main()
    vis.draw()
    again = vis.end()
    if not again: break

