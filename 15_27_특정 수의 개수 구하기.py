'''
n개의 수들이 정렬된 배열이 주어졌을때  x가 몇번 나타나는지 O(logN)의 복잡도 내에서 구하는 코드를 짠다. 
'''
#[내가 짠 코드]
# x가 처음에 나타나는 인덱스를 구한뒤 for문을 이용해서 x가 아닌 수가 나타날때까지 cnt를 +1 하는 코드를 짬
# for 문을 이용해버려서  O(logN)을 만족 못함

#### 이진 탐색을 이용해서 x가 마지막으로 나타는 인덱스를 구해서 처음 나타난 인덱스를 뺀다면 그것이 답

n, x =map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
start = 0
end = n-1
index = 0
while(start<end):
  mid = (start+end)//2
  if arr[mid]>=x:
    end = mid
  else:
    start = mid+1
cnt = 0
for i in range(end,n):
  if arr[i]!=x:
    break
  cnt+=1

print(cnt if cnt!=0 else -1)

#[정답 코드]
# bisect를 이용하면 더 빠름

import bisect
n, x =map(int,input().split())
arr = list(map(int,input().split()))
print(bisect.bisect_right(arr,x)-bisect.bisect_left(arr,x))

