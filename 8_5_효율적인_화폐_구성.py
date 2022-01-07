'''
p.226
배수가 아닌 화폐단위들을 이용하여 목표 금액을 맞추는 최소한의 화폐 개수를 구하는 문제
# 배수 단위가 아니기 때문에 그리드 문제처럼 풀 수x
이 전 값(목표 금액에서 화폐 단위를 뺀 수)에서 1을 더하면 그것이 최소한의 개수
계속해서 수정되면서 원래 저장된 값보다 더 큰 수가 저장될 수 있기 때문에 min 함수를 이용하여 arr[i] 비교해야함.
'''

n, m = map(int,input().split())
arr = []
for i in range(n):
  arr.append(int(input()))

#한 번 계산된 결과를 저장하기 위한 dp 테이블 초기화
d = [10001]*(m+1)

#다이나믹 프로그래밍 진행(보텀업)
d[0] = 0
for i in range(n):
  for j in range(arr[i],m+1):
    if d[j - arr[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
      d[j] = min(d[j], d[j-arr[i]] + 1)

      #계산된 결과 출력
if d[m] == 10001:
  print(-1)
else:
  print(d[m])
