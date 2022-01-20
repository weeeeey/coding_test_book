'''
n개의 집의 위치가 주어졌을때 c개의 공유기를 한 집당 한개씩 설치한다고 가정한다.
이때 공유기를 설치한 집들 사이의 거리를 최대로 잡고 싶을때
그 최대 거리를 출력
'''
# 저번주에 따로 백준사이트에서 풀었던거라 빠른 시간안에 풀 수 있었음

#[내 풀이]
import bisect
n, c = map(int,input().split())
arr =[] #집 위치
for i in range(n):
  arr.append(int(input()))
arr.sort()
max_d = arr[-1]-arr[0]
if c==2:
  print(max_d)

else:
  start = 1
  end = max_d
  result = 0
  while(start<end):
    cnt = 1
    mid = (start + end)//2
    s = arr[0]
    for i in range(1,n):
      if s+mid <=arr[i]:
        s=arr[i]
        cnt+=1
    if cnt<c:
      end = mid
    else:
      start = mid+1
      result = mid  
        
  print(result)
      

    
    
