'''
[문제]
p.115
8*8 체스판에서 위치가 주어졌을경우 나이트가 이동할 수 있는 경우의 수를 구한다
'''

loc = list(input())
a = ord(loc[0]) - 97
b = int(loc[1]) - 1


dx = [1,1,-1,-1,2,2,-2,-2]
dy = [2,-2,2,-2,1,-1,1,-1]
gr = [[0]*8 for i in range(8)]
cnt = 0
gr[a][b] = 1

for i in range(8):
  nx = a + dx[i]
  ny = b + dy[i]
  if nx<0 or nx >7 or ny<0 or ny>7:
    continue
  if gr[nx][ny] != 0:
    continue
  cnt+=1
print(cnt)

#처음 위치에서 계속 이동 할 수 있는 경우의 수를 구하는 줄 알고 BFS로 풀어버렸다. 당연히 63이 나와버렸음.
#문제를 잘 읽어보장
