'''
[문제]
p.152 
2차원 그래프 상에서 1인 부분만을 이동하여 n,m 에 도착하는 최단 경로 구하기
'''
# DFS로 풀까 싶었지만 그럼 리얼 완전 탐색을 해야 하기 떄문에 
# 제일 먼저 도착하는 경우 종료해버리는 BFS로 풀이 했다.

from collections import deque
n, m = map(int,input().split())
gr =[]
for i in range(n):
  gr.append(list(map(int,input())))
visited=[[0]*m for i in range(n)]
q=deque()
q.append((0,0))
visited[0][0] = 1
dx = [1,0,-1,0]
dy = [0,1,0,-1]

while(q):
  x, y = q.popleft()
  if x==(n-1) and y==(m-1):
    print(visited[x][y])
    break  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx >= n or ny >= m :
      continue 
    if visited[nx][ny] > visited[x][y]+1:
      continue
    if gr[nx][ny] == 1 :
      q.append((nx,ny))
      visited[nx][ny] = visited[x][y] + 1 
      
