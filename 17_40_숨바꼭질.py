'''
동빈이가 1~N번까지의 헛간 중에서 하나를 골라 숨을때 1번 헛간으로부터 최단 거리가 가장 먼 헛간에 숨는다고 한다.
이때의 헛간 번호와 최단 거리, 그리고  만약 같은 값이 존재한다면 해당 헛간의 갯수를 출력
#양방향 통로이다.
'''
import heapq
INF = 1e9
n, m = map(int,input().split())
gr = [[] for i in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  gr[a].append(b)
  gr[b].append(a)
q = []
heapq.heappush(q,(0,1))
distance = [INF]*(n+1)
distance[1] = 0
while(q):
  dis, x = heapq.heappop(q)
  for node in gr[x]:
    if distance[node] > dis+1:
      distance[node] = dis+1
      heapq.heappush(q,(dis+1,node))

distance = distance[1:n+1]
for i in range(n):
  distance[i] = (distance[i],i+1)

cnt = 0
distance.sort(key = lambda x:(-x[0],x[1]))
for i in range(1,len(distance)):
  if distance[0][0] == distance[i][0]:
    cnt+=1
  else: 
    break
if cnt == 0:
  cnt = 0
else:
  cnt+=1
print(distance[0][1], distance[0][0], cnt)
