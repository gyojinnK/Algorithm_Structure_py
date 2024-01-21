'''
n개의 도시가 몇 개의 항공편으로 연결되어 있습니다.
항공편[i] = [fromi, toi, Pricei]는
비용이 i인 도시 fromi에서 도시 toi까지의 항공편이 있음을 나타내는 배열 항공편이 제공됩니다.
또한 세 개의 정수 src, dst 및 k가 주어지며 최대 k 정거장을 사용하여 src에서 dst까지
가장 저렴한 가격을 반환합니다. 해당 경로가 없으면 -1을 반환합니다.
'''
import collections
import heapq
from pprint import pprint
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = int(1e9)
        routes = collections.defaultdict(list)
        dist = [[INF] * (n) for _ in range(n)]
        # for f, t, p in flights:
        #     routes[f].append((t, p))
        #
        # pprint(routes)

        for i in range(n):
            dist[i][i] = 0

        for f, t, p in flights:
            dist[f][t] = p

            for a in range(n):
                for b in range(n):
                    dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])



        pprint(dist)

print(Solution().findCheapestPrice(4,
                                   [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
                                   0, 3, 1))