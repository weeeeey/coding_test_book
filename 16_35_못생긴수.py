'''
못생긴 수란 2,3,5 만을 소인수로 가지는 수를 의미한다.
즉 2,3,5를 약수로 가지는 합성수
1 또한 못생긴 수라고 가정했을때
n번째 못생긴 수를 찾는 프로그램을 짜기
'''
# 2,3,5 를 약수로 가진다는건 2,3,5에 각각 2,3,5배를 계속해서 한다는 것과 같다
# 즉 각각의 수에 계속해서 2,3,5를 곱해주면서 기억해두면 됨.
# 나는 BFS 방식을 취함

from collections import deque
s = [1,2,3,5]
q = deque()
q.append(2)
q.append(3)
q.append(5)
dx = [2,3,5]
while(True):
  node = q.popleft()
  if len(s) >= 1001:
    break
  for i in range(3):
    next_node = node*dx[i]
    if next_node in s:
      continue
    s.append(next_node)
    q.append(next_node)

n = int(input())
s.sort()
print(s[n-1])
