'''
가사에 쓰인 단어들의 배열(words)이 주어졌을때
해당 키워드들이 (queries) 각각 몇번 쓰였나 알아보는 문제
이때 키워드에 담겨진 '?'는 와일드카드로써 모든 문자로 대체 가능함
'''
# 해당 키워드를 각각의 가사 단어들마다 이진 탐색으로 풀어봄
# 길이가 다르면 일단 아웃시키고
# 길이가 같고 가운데 단어부터 체크하면서 맞다면 mid값 이전 ,mid값 이후 값들을 재귀를 통해 풀어봄
# 정확성으로는 만점을 받았지만 효율성으로는 1가지 케이스를 제외한 나머지에서 시간 초과 판정을 받음



#[내가 짠 코드 1번]
word = (input().split())
query = input().split()

def solution(w, q): #  w:가사에 담긴 단어들의 배열 , q:찾고자 하는 키워드가 담긴 배열   
  answer = [0]*(len(q))
  for i in range(len(q)):
    cnt = 0
    start = 0
    end = len(q[i])-1
    for j in w:
      if len(q[i]) != len(j):
        continue
      else:
        cnt += binary(q[i],j,start,end)
    answer[i] = cnt
  return answer

def binary(qrr,wrr,s,e):
  if s>e: return None 
  if s==e and (qrr[s] =='?' or qrr[s]==wrr[s]):
    return 1   
  elif s==e and qrr[s]!=wrr[s]:
    return 0
  
  mid = (s+e)//2  
  if qrr[mid] =='?' or qrr[mid]==wrr[mid]:
    left = binary(qrr,wrr,s,mid)
    right = binary(qrr,wrr,mid+1,e)
    if left == 1 and right == 1:
      return 1
    else:
      return 0
  else:
    return 0

print(solution(word,query))


#-----------------------------------
#-----------------------------------

#[내가 짠 코드 2번]
#?를 만났을때 그 이전값이나 이후값이 ? 일 경우 그 방향은 쭉 ?니까 검사할 필요 x 
# 효율성을 올리기 위해서는 이걸 이용하면 될거라 생각함
# 하지만 aaaaa 와 ????o 를 비교했을때도 1이 나와버림
# 이것을 해결해주면 될듯

#응 안돼

#-----------------------------------
#-----------------------------------


#[정답 코드]
# 처음에 bisect 를 활용할려고 했었는데 원하는 인덱스가 안떠서 실패했었다
# 왜그랬지?
# 접미사나 접두사에 ? 가 온다느걸 활용했어ㅑ함
# 물음표를 a와 z로 바꾸는 센스

from bisect import bisect_left,bisect_right
arr = [[] for i in range(10001)] #모든 단어를 길이에 따라 나누어서 저장하기 위함
r_arr = [[] for i in range(10001)] #와일드카드가 앞에서부터 나오는 경우를 위해 존재
word = input().split()
query = input().split()

def count_by_range(a, left_v, right_v):
  left_index = bisect_left(a,left_v)
  right_index = bisect_right(a,right_v)
  return right_index - left_index

def solution(w,q):
  ans = []
  for word in w:
    arr[len(word)].append(word) #가사 단어를 삽입
    r_arr[len(word)].append(word[::-1]) #단어를 뒤집어서 삽입
  for i in range(10001):
    arr[i].sort()
    r_arr[i].sort()
  for query in q:
    if query[0] != '?': #접미사에 ?가 붙운 경우
      res = count_by_range(arr[len(query)],query.replace('?','a'),query.replace('?','z') )
    else:
      res = count_by_range(r_arr[len(query)],query[::-1].replace('?','a'),query[::-1].replace('?','z') )
    ans.append(res)
  return ans
print(solution(word,query))


