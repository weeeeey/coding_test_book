'''
[문제]
p.149
2차원 그래프상에서 1은 벽, 0은 얼음 이라고 가정
이떄 0끼리 이어진 얼음 모양을 만든다면 총 몇개를 만들수 있는가

DFS로 풀려고 마음 먹었는데 풀다보니 BFS가 되어버렸다. 
그래서 둘 다 작성
'''
#BFS 
from collections import deque
n, m = map(int,input().split()) # n 세로 , m 가로
gr= [[0]*m for i in range(n)]
for i in range(n):
  gr[i] = list(map(int,input()))
cnt = 0
    
def BFS(a,b):
  gr[a][b] = 1
  q = deque()
  q.append((a,b))
  dx = [0,0,-1,1]
  dy = [-1,1,0,0]  
  while(q):
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx <0 or ny <0 or nx>=n or ny>=m:
        continue
      if gr[nx][ny] == 0 :
        gr[nx][ny] = 1
        q.append((nx,ny))

for i in range(n):
  for j in range(m):
    if gr[i][j] == 0:
      cnt+=1
      print(i,j)
      BFS(i,j)

'''
아래는 DFS
'''
n, m = map(int,input().split()) # n 세로 , m 가로
gr= [[0]*m for i in range(n)]
for i in range(n):
  gr[i] = list(map(int,input()))
cnt = 0
    
def DFS(a,b): #책에서는 dfs(a-1,b) , dfs(a+1,b) , dfs(a,b-1), dfs(a,b+1) 을 
  gr[a][b] = 1
  dx = [0,0,-1,1]
  dy = [-1,1,0,0]
  for i in range(4):
    nx = a + dx[i]
    ny = b + dy[i]
    if nx < 0 or ny <0 or nx >= n or ny >= m:
      continue
    if gr[nx][ny] == 0:
      DFS(nx,ny)

for i in range(n):
  for j in range(m):
    if gr[i][j] == 0:
      cnt+=1
      DFS(i,j)
print(cnt)

