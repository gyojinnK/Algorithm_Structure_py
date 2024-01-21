'''
1부터 n까지 레이블이 지정된 n개의 노드로 구성된 네트워크가 제공됩니다.
또한 방향이 지정된 가장자리로 이동 시간 목록인 시간이 제공됩니다.
times[i] = (ui, vi, wi), 여기서 ui는 소스 노드, vi는 대상 노드, wi는 신호에 걸리는 시간입니다.
소스에서 타겟으로 이동합니다.
주어진 노드 k에서 신호를 보냅니다.
n개 노드 모두가 신호를 수신하는 데 걸리는 최소 시간을 반환합니다.
n개의 노드 모두가 신호를 수신하는 것이 불가능하면 -1을 반환합니다.
'''
import collections
import heapq
from pprint import pprint
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = collections.defaultdict(list)

        for nInfo in times:
            network[nInfo[0]].append((nInfo[2], nInfo[1]))

        q = []
        heapq.heappush(q, (0, k))
        dist = collections.defaultdict(int)

        while q:
            acc, curr = heapq.heappop(q)
            if curr not in dist:
                dist[curr] = acc
                for d, adj in network[curr]:
                    cost = acc + d
                    heapq.heappush(q, (cost, adj))

        return max(dist.values()) if len(dist) == n else -1

print(Solution().networkDelayTime([[1,2,1],[2,1,3]], 2, 2))
