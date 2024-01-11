# L: L개의 알파벳
# C: 주어지는 문자의 수
from itertools import combinations

L, C = map(int, input().split(' '))
alphas = sorted(list(map(str, input().split(' '))))
check_vowels = ['a', 'e', 'i', 'o', 'u']

res = []
combi = combinations(alphas, L)

for el in combi:
    vowels_checker = 0
    consonants_checker = 0
    for t in el:
        if t in check_vowels:
            vowels_checker += 1
        if t not in check_vowels:
            consonants_checker += 1
    if vowels_checker >= 1 and consonants_checker >= 2:
        res.append(el)
print(res)
for el in res:
    print(''.join(t for t in el))
