from pyvisalgo import QuickSortVisualizer as Visualizer
# from pyvisalgo import Dummy as Visualizer
from time import time
from random import randint, seed, shuffle

def main():
  # print('before:', array)
  count = len(array)
  quickSort(0, count-1)
  # insertionSort(0, count-1)

  # print('after :', array)

def quickSort(left, right): #q=inclusive
  if left == right: vis.fix(left)  # 정렬 대상이 하나뿐이라면 확정해도 좋다
  if left >= right: return         # 정렬할 것이 없으면 할 일이 없다
  # if right < left + 4:
  #   # insertionSort(left, right)
  #   return
  vis.push(left, right)
  pivot = partition(left, right)   # pivot 위치를 결정해 온다
  vis.set_pivot(pivot)
  quickSort(left, pivot-1)  # pivot 보다 왼쪽 그룹을 다시 quickSort 한다
  quickSort(pivot+1, right) # pivot 보다 오른쪽 그룹을 다시 quickSort 한다
  vis.pop()

def insertionSort(left, right): #right=inclusive
  for i in range(left + 1, right + 1):
    v = array[i]
    vis.mark_end(i, v)
    j = i - 1
    while j >= left and array[j] > v:
      vis.shift(j)
      array[j+1] = array[j]
      j -= 1
    vis.insert(i, j+1)
    array[j+1] = v

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

  return q  # 결정된 pivot 의 위치를 리턴한다

''' 성능 측정
# QuickSort           Normal 2-Swap  4-Ins 
count=100     elapsed= 0.000  0.000  0.000 
count=1000    elapsed= 0.003  0.002  0.002 
count=2000    elapsed= 0.005  0.005  0.005 
count=3000    elapsed= 0.007  0.007  0.007 
count=4000    elapsed= 0.010  0.010  0.010 
count=5000    elapsed= 0.013  0.013  0.013 
count=6000    elapsed= 0.015  0.015  0.015 
count=7000    elapsed= 0.021  0.021  0.020 
count=8000    elapsed= 0.021  0.024  0.022 
count=9000    elapsed= 0.023  0.026  0.024 
count=10000   elapsed= 0.030  0.031  0.025 
count=15000   elapsed= 0.043  0.042  0.041 
count=20000   elapsed= 0.059  0.059  0.053 
count=30000   elapsed= 0.096  0.103  0.090 
count=40000   elapsed= 0.125  0.116  0.117 
count=50000   elapsed= 0.156  0.141  0.156 
count=100000  elapsed= 0.419  0.344  0.351 
count=200000  elapsed= 0.690  0.730  0.644 
count=300000  elapsed= 1.115  1.087  1.031 
count=400000  elapsed= 1.670  1.540  1.450 
count=500000  elapsed= 2.235  2.172  2.051 
count=1000000 elapsed= 4.496  4.747  4.017 
count=2000000 elapsed= 9.740  9.629  8.934 
count=3000000 elapsed=15.635 15.486 14.271 
count=4000000 elapsed=20.053 19.965 18.831 
count=5000000 elapsed=26.747 25.844 24.089 
'''
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

