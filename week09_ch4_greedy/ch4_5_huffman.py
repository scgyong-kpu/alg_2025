from collections import defaultdict

with open('data_knapsack.json') as f:
  contents = f.read()
  print(f'{len(contents)=}')

counts = defaultdict(int)
for ch in contents:
    counts[ch] += 1
    # ch 가 key 로 존재하지 않으면 int() 가 수행되어 값이 들어간다
    # dict 의 KeyError 를 피할 수 있는 편리한 방법이다

print(counts)
