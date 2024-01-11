
from itertools import combinations_with_replacement

data = [1, 2, 3]

# combinations_with_replacement(iterable 객체(ex. list...), 뽑을 요소 수)
result = list(combinations_with_replacement(data, 3))
print(result)