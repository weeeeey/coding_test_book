'''
[문제]
p.118 

'''
n, m = map(int,input().split()) # n 행 m 열
gr = [[] for i in range(n)]
loc = list(map(int,input().split()))
for i in range(n):
  gr[i]= list(map(int,input().split()))
gr[loc[0]][loc[1]]=1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
while():
  cnt = 0 
  loc[2]-=1
  if loc [2] == -1:
    loc[2]==3
  nx = loc[0] + dx[loc[2]]
  ny = loc[1] + dy[loc[2]]
  if 0<= loc[0] <n and 0<=loc[1]<=m:        
    if gr[nx][ny] == 0 :
      loc[0],loc[1] = nx,ny
      gr[nx][ny] = 1
    elif gr[nx][ny] == 1:
      if cnt < 4:
        loc[2]-=1
        cnt+=1
      else:
        if loc[2] == 0:
          loc[0]+=1 
        elif loc[2] == 1:
          loc[1] -=1
        elif loc[2] == 2:
          loc[0] -=1     
        else:
          loc[1] +=1
        if loc[0]<0 or loc[1]<0 or loc[0]>n or loc[1]>n:
          break
        if gr[loc[0]][loc[1]] == 1:
          break
        cnt=0
