'''
입력된 괄호로 이루어진 문자열을 짝을 맞추어 출력하는 알고리즘
재귀 개념이 포함되어서 DFS 컨텐츠에 포함 되어 있지만 구현 문제에 가깝다.
'''
# 분리 하는 것과 올바른 문자열인지 확인하는 과정이 여러번 반복되어
# 따로 함수를 만들면 되겠다고 생각해서 짰음
# sol함수를 재귀적으로 푸는게 맞다고 생각했지만 return 값의 위치를 잘못 잡아서 틀림
# str 타입은 + 연산으로 간단하게 이을 수 있다는걸 간과함 

from collections import deque
w = input()
def sec(ini): #u,v로 분리
  cnt_left = 0
  cnt_right = 0
  q = deque()
  for i in ini:
    q.append(i)
    if i == '(' : cnt_left += 1
    else: cnt_right+=1 
    if cnt_left == cnt_right: 
      return len(q)
      
def cor(ini): #올바른 문자열인지 확인
  if ini[0] == ')' or not ini: return False
  q = []
  for i in ini:
    if i == '(': q.append(i)
    else: q.pop()
  if not q: return True
  else : return False

  
def sol(p):
  answer = ''
  if p =='':
    return answer
  index = sec(p)
  u = p[:index]
  v = p[index:]
  if cor(u):
    answer = u + sol(v)
  else:
    answer = '('
    answer += sol(v)
    answer += ')'
    u = list(u[1:-1])  #첫 번째와 마지막 문자 제거
    for i in range(len(u)):
      if u[i] =='(':
        u[i] =')'
      else:
        u[i] = '('
    answer += "".join(u)
  return answer
print(sol(w))
