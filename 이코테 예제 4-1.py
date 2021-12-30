'''
[문제 풀이]
크기가 num*num인 그래프 상에서 
(1,1) 에서 출발하여 이동방향 (L R U D)에 따라 좌표 설정
(그래프 범위 벗어날시 무시 )
'''


num = int(input())
gr = [[0]*(num+1) for i in range(num+1)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
path = ['L','R','U','D']
x,y = 1, 1
dic = input().split()
dic.reverse()       # queue가 아니어서 popleft못쓰므로 리버스

while(dic):
  z = dic.pop()
  loc = path.index(z)
  nx = x + dx[loc]
  ny = y + dy[loc]
  if 0<nx<num and 0<ny<num:
    x,y = nx,ny
print( x, y )
