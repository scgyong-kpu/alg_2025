import json
with open('data_knapsack.json') as f:
  mats = json.load(f)
print(f'{mats=}')

# python 의 내장모듈 json 을 활용하여 json 파일을 로드하여 
# mats 라는 이름의 dict 변수 에 저장한다.
