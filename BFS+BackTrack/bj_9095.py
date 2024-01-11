def bt(value, sum):
    global cnt
    # 현재 합이 n 이상이면 중단
    if sum >= n:
        return
    sum += value
    # n에 도달하면 count 증가
    if sum == n:
        cnt += 1

    # 각 경우의 수로 백트래킹 함수 재귀적으로 호출
    bt(1, sum)
    bt(2, sum)
    bt(3, sum)

cnt = 0   # 유효한 조합의 수

T = int(input())
for i in range(T):
    n = int(input())
    cnt = 0   # n이 완성된 횟수
    bt(0, 0)
    print(cnt)


