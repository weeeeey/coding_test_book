'''
n개의 볼링공이 주어지는데 이때 각각의 볼링공의 무게는 1~m 까지 해당된다.
이때 각각의 볼링공을 2개씩 든다고 가정했을때 이때 번호가 다르더라도 무게가 같다면 같은 볼링공으로 간주하여 경우의 수에서 제외한다.
최대 만들 수 있는 경우의 수는?
'''
# 처음에 문제를 받았을때 범위도 낮아서 구할 수 있는 모든 경우의 수를 구한 다음, 같은 무게의 공이라면 제외 하는 프로그램 짬.
# 이를 좀 더 수학적이고 그리드 문제식으로 접근하는 방식이 책에서 소개됨

#[조합을 이용해서 짠 내 코드] 
import itertools
n,m = map(int,input().split())
arr = list(map(int,input().split()))
a = []
for i in range(n):
  if arr[i]!=0:
    a.append(i+1)
result = [[False]*(n+1) for i in range(n+1)]
temp = list(itertools.combinations(a,2))
cnt=0
for i in temp:
  if arr[i[0]-1] != arr[i[1]-1]:
    result[i[0]][i[1]] = True
for i in range(1,n+1):
  for j in range(1,n+1):
    if result[i][j] == True:
      cnt+=1
print(cnt)

# [그리드하게 접근]
# 각각의 볼링공을 무게마다 몇개씩 있는지 체크
# 볼링공의 무게에 따라 경우의 수가 나눠지기 때문
# a가 특정 공을 선택 했을때, b가 고를 수 있는 경우의 수를 구한다.
# 예를 들어 1,2,2,3,3 인 공이 주어졌을때
# a가 무게가 1인 공을 고르는 경우의 수는 1 -> 이떄 b가 고를 수 있는 경우의 수는 2(2번),2(3번),3(4번),3(5번) 총 4가지 이다 => 1*4
# a가 무게가 2인 공을 고르는 경우의 수는 2 -> 이떄 b가 고를 수 있는 경우의 수는 3(4번),3(5번) 총 2가지 이다. => 2*2 (1번을 제외한 이유는 위에 포함 되어 있기 때문)
# a가 무게가 3인 공을 고르는 경우의 수는 2 -> 이떄 b가 고를 수 있는 경우의 수는 x 총 0 가지 => 2*0 
# 이들을 모두 더하면 8이 된다.


n,m = map(int,input().split())
arr = list(map(int,input().split()))
temp =[0]*(m+1)
for i in arr:
  temp[i] += 1 #무게별로 갯수 구해줌
cnt = 0
for i in range(1,m+1):
  n -= temp[i] #현재까지의 갯수를 제외한 나머지 값들
  cnt += temp[i]*n #현재 갯수 * 나머지 갯수
print(cnt)








