'''
p.201
n : 떡의 갯수
m : 가져갈려는 떡의 총길이
n,m을 입력받은 후 
저장되어 있는 떡의 정보에서 손님이 요청한 길이를 뗴줘야함
'''
#[처음에 풀었던 방식]
n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
start = 0
end = len(arr)-1
sum = 0
height = arr[(start+end)//2]  #이진탐색 파트에 있으니까 미들값을 사용하고 싶은데 그것을 단순하게 중간값으로 자르고 그 합이 더 크면 중간값의 +1을 하거나 -1 을 하는 단순 작업을 함
                              #제한점이 20억이기 때문에 실제 사이트였다면 시간 초과 날 듯
while( True ):
  sum = 0  
  for i in range(n):
    cnt = arr[i]-height
    if cnt < 0 :
      cnt = 0
    sum += cnt
  if sum == m :
    break
  if sum > m:
    height += 1
  else:
    height -= 1

print(height)

'''
'''
#[책에서 제시한 답]
#어쨌든 잘라져야 하기 때문에 가장 긴 떡보다는 작을 것이다.
#그러므로 가장 긴 떡을 기준으로 그 중간 값부터 잘라보고 합이 더 크다면 다시 끝점과 중간값+1의 평균을 구해서 하다보면 결국 최대 31번을 계산하므로 더 효율적

n, m = map(int,input().split())
arr = list(map(int,input().split()))
standard = max(arr)
start = 0
end = standard
while( start <= end ):
  height = (start+end)//2
  sum = 0
  for i in range(n):
    sr = (arr[i]-height)
    if sr<0:
      sr = 0
    sum+=sr
  if sum == m:
    break
  if sum > m:
    start = height + 1
  else:
    end = height - 1
print(height)
