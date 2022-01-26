'''
n*n크기의 공간에 각 칸에 대한 지나가면서 내야할 비용을 표시한다.
0,0 에서 출발하여 n-1,n-1에 도착할때 
가장 최소의 비용을 출력하는 프로그램을 짜기
상하좌우 움직임
'''
# 현재 좌표까지 오는 비용을 우선순위 큐의 기준으로 두는 프로그램을 짬
import heapq
INF = 1e9
n = int(input())
gr = [[0]*n for i in range(n)]
for i in range(n):
  gr[i] = list(map(int,input().split()))
visited = [[False]*(n) for i in range(n)]
q = []
heapq.heappush(q,((gr[0][0],0,0)))
visited[0][0] = True
dx = [1,0,-1,0]
dy = [0,1,0,-1]
while(q):
  dis,x,y = heapq.heappop(q)
  if (x,y) == (n-1,n-1):
    print(dis)
    break
 
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx<0 or ny<0 or nx>=n or ny>=n:
      continue
    if visited[nx][ny] ==False:
      visited[nx][ny] = True
      heapq.heappush(q,((dis+gr[nx][ny],nx,ny)))

