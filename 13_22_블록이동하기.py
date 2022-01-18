'''
2*1의 크기를 가진 로봇이 (0,0)(0,1)에서 출발 했을때 오른쪽 최하단에 도착하는 최단 거리를 출력하는 문제
0인 칸만 지날수 있음.
돌렸을때 1인 칸이 없다면 90도 회전도 가능 
'''
# 내가 짠 코드 - 프로그래머스에서 돌리면 한 테스트일 경우 시간 초과가 뜸
from collections import deque

def solution(gr):
    n = len(gr)
    visit = []
    q = deque()
    q.append(((0,0),(0,1),0))
    visit.append(((0,0),(0,1)))
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1] #move
    dz = [-1,1] #spin
    while(q):
        tail, head, count = q.popleft()
        form = 0 if tail[0]==head[0] else 1
        if head == (n-1,n-1)or tail== (n-1,n-1):  
          return count
            
        tx,ty,hx,hy = tail[0],tail[1],head[0],head[1]
        for i in range(4): #그대로 상하좌우 movs
            n_tx = tx + dx[i]
            n_ty = ty + dy[i]
            n_hx = hx + dx[i]
            n_hy = hy + dy[i]
            if n_hx<0 or n_hy<0 or n_tx<0 or n_ty<0 or n_hx>=n or n_hy>=n or n_tx>=n or n_ty>=n:
                continue
            if gr[n_hx][n_hy] == 0 and gr[n_tx][n_ty] == 0:
                if ((n_tx,n_ty),(n_hx,n_hy)) not in visit:
                    q.append(((n_tx,n_ty),(n_hx,n_hy),count+1))
                    visit.append(((n_tx,n_ty),(n_hx,n_hy)))

        #spin
        if form == 0: #가로 모양,x좌표만 신경쓰면 됨
          for i in range(2):
            ntx = tx + dz[i]
            nhx = hx + dz[i]
            if ntx <0 or nhx<0 or ntx>=n or nhx>=n: continue
            if gr[ntx][ty] == 0 and gr[nhx][hy] == 0 :
              if ((ntx,ty),(tx,ty)) not in visit:
                q.append(((ntx,ty),(tx,ty),count+1))
                visit.append(((ntx,ty),(tx,ty)))
              if ((nhx,hy),(hx,hy)) not in visit:
                q.append(((nhx,hy),(hx,hy),count+1))
                visit.append(((nhx,hy),(hx,hy)))
        if form == 1: #세로 모양, y좌표만 신경쓴다.
          for i in range(2):
            nty = dz[i] + ty
            nhy = dz[i] + hy
            if nty<0 or nhy<0 or nty>=n or nhy>=n: continue
            if gr[tx][nty] == 0 and gr[hx][nhy] == 0 :
              if ((tx,ty),(tx,nty)) not in visit:
                q.append(((tx,ty),(tx,nty),count+1))
                visit.append(((tx,ty),(tx,nty)))
              if ((hx,hy),(hx,nhy)) not in visit:
                q.append(((hx,hy),(hx,nhy),count+1))
                visit.append(((hx,hy),(hx,nhy)))
