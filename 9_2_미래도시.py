'''
p.259
n개의 도시와 m개의 이동 경로가 주어졌을때
1번 도시에서 출발하여 k 도시를 거친 후 x 도시에 도착하는 최단 경로를 구하는 문제
'''
# 1번에서 출발하여 k도시를 거친후 x 도시를 도착하는 것이니
# 일단 1번에서 k까지의 경로룰 구한다
# 이후 출발 지점을 k라고 생각하고 x 도시를 가는 경로를 구한다
# 그 두개의 답을 더한다. 
# 처음에는 그 두개의 답을 곱했는데 그것은 k까지 도달하는 여러 경우가 있고 x까지 도달하는 여러 경우가 있을 경우 곱해주는것이다.
# 이 경우에는 k까지 도달하는 최단 경로는 1가지 이고 ( 간선의 수치가 다를뿐)
# k에서 x까지 도달하는 경로는 1가지 이므로 더하는게 맞다. 

import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

n, m = map(int,input().split())
gr = [[] for i in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  gr[a].append(b)
  gr[b].append(a)
x, k = map(int,input().split()) #k번 갔다가 x번 회사 가야함       

def dikstra( start, destiny ):
  distance = [INF]*(n+1)
  distance[start] = 0
  q = []
  heapq.heappush(q,start)
  while(q):
    node = heapq.heappop(q)
    dis = distance[node]
    for i in gr[node]:
      if distance[i] > dis+1:
        distance[i] = dis + 1
        heapq.heappush(q,i)
  return distance[destiny] if distance[destiny] != INF else -1
dis_1 = dikstra(1,k)
dis_2 = dikstra(k,x)
print(dis_1 + dis_2 if (dis_1 != -1) and (dis_2 != -1) else -1)

