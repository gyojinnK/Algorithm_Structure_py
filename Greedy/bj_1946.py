import sys

input = sys.stdin.readline

t = int(input())
res = []
for _ in range(t):
    n = int(input())    # 지원자 수

    scoreInfos = []
    # 서류, 면접 성적
    for _ in range(n):
        doc, interview = map(int, input().split())
        scoreInfos.append((doc, interview))

    # 서면 등수가 낮은 순으로 정렬
    scoreInfos.sort()

    interviewScores = []
    for el in scoreInfos:
        _, score = el
        interviewScores.append(score)

    bestIdx = 0
    # 첫번째는 무조건 채용 (서류 점수가 1등이기 때문)
    # ==> 합격자 수를 1로 시작
    passCnt = 1
    # 다음 참가자 중 자신의 순위 보다 높은 순위가 있으면 -
    for i in range(1, n):
        # 돌다가 현재 최고점 보다 작으면(순위가 높으면)
        if interviewScores[bestIdx] > interviewScores[i]:
            passCnt += 1
            # 현재 탐색까지 중 면접 점수가 가장 높은 점수로 갱신
            bestIdx = i

    res.append(passCnt)

print('\n'.join(str(el) for el in res))
