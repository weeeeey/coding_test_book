# 빅오 표기법은 최악의 시간 복잡도를 표시 하는것 
# 세타 표기법: 평균복잡도
# 오메가 표기법 : 최선의 시간 복잡도
# cf) 퀵소트의 평균은 (n)log(n), 최악은 n^2 => 따라서 퀵솟은 O(nlog(n))
# cf) 파이썬의 기본 정렬 라이브러리는 내부적으로 c언어를 기반으로 최적화 되어 있음. (퀵보다도 더 빠르다)
'''
[선택정렬]
첫번쨰 인덱스부터 순서대로 피벗으로 삼아 그 다음 수중 최소값을 해당 인덱스와 스왑 (비교 시 arr[피벗] 도 포함 )
O(n^2)
n+(n-1)+(n-2)+...+2 => O(n^2)
'''
arr = [2,42,6,7]
for i in range(len(arr)):
  min_t = i
  for j in range(i+1,len(arr)):
    if arr[min_t]>arr[j]:
      min_t=j
  arr[i] ,arr[min_t] = arr[min_t], arr[i]
  
  
'''
[삽입 정렬]
선택 정렬에 비해 실행 시간 효율적
필요할 때만 위치를 바꿈 ( 정렬된 상태일떄 최적화 ) - > 오메가(n)
피벗 이전 데이터들은 정려된 상태라고 가정
피벗값보다 작을 경우 (오름차순 일 경우) 피벗부터 시작하여 이전 값들과 비교
큰 값을 찾기 전까지 위치를 바꾸어준다
O(n^2)
'''
arr = [2,42,6,7]
for i in range(1,len(arr)):
  for j in range(i,0,-1):
    if arr[j] < arr[j-1]:
      arr[j],arr[j-1] = arr[j-1],arr[j]
    else:
      break

'''
[퀵소트]
정렬 알고리즘 중 가장 많이 사용된다
피벗을 기준으로 왼쪽에는 피벗보다 작은, 오른쪽에는 피벗보다 큰 (오름차순 기준)
만약 left가 right 보다 커졌을시 작은 값과 피벗 위치를 변경
시간 복잡도 n^2 
오메가, 세타 복잡도 n logn

'''
# if 문 내에서 조건도 순차적으로 적용된다는걸 알게 됨. 
# (a 조건), (b 조건) 이 있을떄, 만약 b 조건 자체가 성립이 안된다면 -> b and a 라고 가정했을시 오류가 되지만 a조건에서 b 조건 자체를 거를 경우 a and b는 실행 됨.
# 피벗은 배열의 맨 처음을 적용한 것
# 파이썬의 장점을 활용해서 코드를 짜고 싶다면 pivot = arr[0] , tail = arr[1:] 을 활용해보자.
arr = [9,8,7,6,5,4,3,2,1]

def quick(arr, start, end ):
  if start >= end :
    return
  pivot = start
  left = start + 1  
  right = end
  
  while ( left <= right):
    while left <= end and ( arr[left] <= arr[pivot] ): # 조건의 순서를 변경하면 디버깅 자체가 안된다 
      left += 1
    while ( right > start ) and ( arr[right] >= arr[pivot] ):
      right -= 1
    if left > right:
      arr[right], arr[pivot] = arr[pivot], arr[right]
    else: 
      arr[left],arr[right] = arr[right], arr[left]
  
  quick(arr, start, right-1)
  quick(arr, right+1, end)

quick(arr, 0, (len(arr)-1) )


'''
[계수 정렬]
특정 조건에서 사용하는 정렬



'''















'''
[파이썬 내부 정렬]
sorted() 나 sort() 함수 같은 경우 퀵과 비슷한 병합 정렬 기반으로 만들어짐.
퀵보다는 느리지만 O(nlogn) 을 가짐. (정확히 말하자면 병합,삽입 정렬의 하이브리드)
매개변수로 key를 가져올 수 있는데 이떄 하나의 함수가 들어가야 정렬 기준이 된다.
아래는 예시이다.
cf) 람다식 이용 가능
cf) 문제에서 별도 요구 없다면 기본 정렬 함수 사용, 데이터의 범위가 한정되어 있다면 계수 정렬 사용

'''
arr = [ ('바나나',7) , ('참외',3), ('사과',5) ] 

def setting(data):
  return data[1]
result = sorted(arr, key = setting)

