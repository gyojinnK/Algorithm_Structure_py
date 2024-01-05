def numJewlsInStones(jewels: str, stones: str) -> int:
    base = {}

    # 해시맵 초기화
    for j in jewels:
        base[j] = 0
    # {'a':0, 'A':0}

    for t in stones:
        if t in base:
            base[t] += 1

    total = 0
    for el in base:
        total += base[el]

    return total

print(numJewlsInStones("z", "ZZ"))