'''
고정점이란 배열에서 인덱스와 해당 인덱스 값이 동일한 것을 맣한다.
arr[2]=2 이면 2는 고정점
주어진 배열에서 O(logN) 의 복잡도로 고정점을 찾아라
없을 경우 -1을 출력
'''
# [내가 짠 코드]
n = int(input())
arr = list(map(int,input().split()))
start = 0
end = n-1
result = n+1
while(start<=end):
  mid = (start+end)//2
  if arr[mid] == mid :
    result = mid
    break
  elif arr[mid]<mid:
    start = mid+1
  else:
    end = mid-1
print(result if result!=(n+1) else -1 )




