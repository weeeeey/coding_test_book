'''
p.262 
특정 도시에서 시작하여 되도록 많은 도시에 메시지를 날려야하는 상황
이때 도시의 개수와 걸리는 시간을 구하시오.

'''
# 처음에는 이동할때마다 나오는 수치를 더해야 한다고 생각함.
# 하지만 이동하는 순간들은 동시다발적으로 이뤄지기 때문에 더하는 것이 아닌
# 특정 지점에서 출발하여 도착할 수 있는 모든 경로들을 구한 뒤
# 이중에서 가장 오래 걸린 시간을 출력하면 됨
# 플로이드로 풀까 했지만 O(n^3)인 알고리즘으로는 노드 개수가 3만 이하인 그래프를 통제하기 힘들다고 생각.
# 더군다나 출발하는 지점은 한개이므로 플로이드를 쓸 이유 x

import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

n, m, s = map(int,input().split()) #n개의 도시, m개의 이동경로, c는 출발지점
gr = [[] for i in range(n+1)]
for i in range(m):
  a,b,c = map(int,input().split())
  gr[a].append((b,c))
cnt = 0
sum = 0
distance = [INF]*(n+1)
distance[s] = 0
q = []
heapq.heappush(q,(0,s))
while(q):
  dis, node = heapq.heappop(q)
  for i in gr[node]:
    if distance[i[0]] > dis+i[1]:
      distance[i[0]] = dis + i[1]
    heapq.heappush(q,(distance[i[0]],i[0]))

for i in range(1,n+1):
  if distance[i] != 0 and distance[i] != INF :
    cnt+=1
    sum = max(distance[i],sum)
print(cnt, sum)
