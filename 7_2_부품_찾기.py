'''
p.197
손님이 주문한 부품이 가게 안에 있다면 yes ,없다면 no 출력

'''
#[ if문을 이용한 순차탐색 ]

import sys 
input = sys.stdin.readline
n = int(input())
n_arr = list(map(int,input().split()))
m = int(input())
m_arr = list(map(int,input().split()))
for i in range(m):
  if m_arr[i] in n_arr:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')
    
# 정렬 후 이진 탐색을 이용한 경우 ( 입력 데이터 제한이 1백만까지라서 1)정렬하고 찾으면 더 괜찮을것이고, 맥스가 1백만이므로 2)계수 정렬을 이용해도 괜찮음

#[ 기본 정렬 후 이진 탐색  ]

import sys 
input = sys.stdin.readline
n = int(input())
n_arr = list(map(int,input().split()))
m = int(input())
m_arr = list(map(int,input().split()))
n_arr.sort()

def binary_search(tar):
  start = 0
  end = len(n_arr)-1
  while ( start <= end ):
    mid = (start+end)//2
    if n_arr[mid] == tar :
      return True
    if n_arr[mid] > tar:
      end = mid - 1
    else:
      start = mid + 1
  return False
for target in m_arr:
  print( 'yes' if binary_search(target) == True else 'no' )
  
  
# [ 계수 정렬 이용 ]

import sys 
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
n_arr = [0]*1000001
for i in range(n):
  n_arr[arr[i]]+=1

m = int(input())
m_arr = list(map(int,input().split()))

for i in m_arr:
  if n_arr[i]>0:
    print('yes')
  else:
    print('no')
  

'''
처음에 풀었던 코드에 집합 자료 set을 이용한다면 n_arr의 크기를 줄일 수 있다.
'''
  
