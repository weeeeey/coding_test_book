'''
[문제]
p.118 
첫 위치에서 반시계 방향으로 회전하면서 
0인 위치만 이동하여 방문한 횟수를 체크하는 문제
'''

n, m = map(int,input().split()) # n 행 m 열
gr = [[] for i in range(n)]     #지도 
visit = [ [False]*m for i in range(n)] #방문한 곳 체크 
loc = list(map(int,input().split()))   #첫 위치

for i in range(n):
  gr[i]= list(map(int,input().split()))

visit[loc[0]][loc[1]]=1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
result = 1 #방문횟수 (첫 장소도 포함)
cnt = 0  #한 자리에서 회전한 수
while():
  if cnt==4:    #사면이 막혔으니 아웃
    break
  
  loc[2]-=1
  cnt+=1
  if loc [2] == -1:
    loc[2]==3

  nx = loc[0] + dx[loc[2]]
  ny = loc[1] + dy[loc[2]]
  
  if nx<0 or ny<0 or nx >n or ny >m:  #바라보는 곳이 바깥이면 한번 더 회전
    cnt+=1
    continue
    
  if gr[nx][ny] == 0 and visit[nx][ny] == 0:
    loc[0],loc[1] = nx,ny
    visit[nx][ny] = 1
    cnt = 0 
    result += 1
    continue 

  if gr[nx][ny] == 1:
    if cnt < 4:
      loc[2]-=1
      cnt+=1
    if cnt == 4:
      if loc[2] == 0: # 뒤로 한칸 이동
        loc[0]+=1 
      elif loc[2] == 1:
        loc[1] -=1
      elif loc[2] == 2:
        loc[0] -=1     
      else:
        loc[1] +=1
      if loc[0]<0 or loc[1]<0 or loc[0]>n or loc[1]>m:  #뒤로 이동했는데 바깥이면 아웃
        break
      if gr[loc[0]][loc[1]] == 1:   # 뒤로 이동한 곳이 1이면 아웃
        break
      cnt=0
      result+=1 
      visit[loc[0]][loc[1]] = 1
      
print(result)


'''
책에서는 그래프 바깥으로 빠지는 경우는 체크 안해줌
코테에서는 입력수가 제한적이기 때문에 굳이 안해도 된다고 쓰여있지만 공부한는 입장이니 다 체크 해보고 싶었다.
'''
