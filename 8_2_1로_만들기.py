'''
p.217 
어떤 수를 입력받았을때  5,3,2로 나누어 떨어지면 그 수로 나누어주고, 불가능하다면 -1을 한다.
일련의 과정을 통해 처음 입력 수를 1로 만드는 최소한의 연산 수는?
'''
# [ 내가 처음에 짠 코드 ]
# BFS 방식으로 풀어버림
from collections import deque
q= deque()
num = int(input())
arr = [0]*(num+1)
dx = [5,3,2,-1]
q.append(num)

while(q):
  x= q.popleft()
  if x == 1:
    break
  for i in range(4):
    nx = 0
    if i != 3 and ( x%dx[i] == 0 ):
      nx = x//dx[i]
    else:
      nx = x-1
    if arr[nx]<=arr[x]+1:
      arr[nx] = arr[x] + 1
      q.append(nx)

print(arr[1])

# [다이나믹 프로그래밍답게 푼 코드]
# 점화식을 이용해서 보텀업 방식 채택 (1이 입력 수가 되기까지 횟수)
# 트리 형탸를 그려보면 이해하기 쉬움
# a(i) = min{a(i-1),a/2,a/3,a/5)}+1
num = int(input())
arr = [0]*(num+1)
for i in range(2,num+1):
  arr[i] = arr[i-1] + 1
  if i%2 == 0:
    arr[i] = min(arr[i],arr[i//2]+1)
  if i%3 == 0:
    arr[i] = min(arr[i],arr[i//3]+1)
  if i%5 == 0:
    arr[i] = min(arr[i],arr[i//5]+1)


  
print(arr[num])
