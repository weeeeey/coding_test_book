'''
총 인원을 입력받은 뒤
각 인원별로 공포도를 입력받는다.
이 인원들로 그룹을 결성할려고 할때, 각 그룹의 인원 수는 해당 그룹원들의 공포도 이상이어야 한다.
이때 최대 만들 수 있는 그룹 수는?
'''
# 최대 그룹 수를 만드는 것이니 공포도가 낮은 잔잔바리들끼리 최대한 모아주어야한다.
# 공포도를 기준으로 오름차순 정렬 후
# 해당 그룹에서의 최대 공포도보다 인원이 그 이상인지 체크
# 2 3 1 2 2 일때
# 1(o)  2,2(o)  2,3(x)

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
result = 0 #총 그룹 수
cnt = 0 #해당 그룹 인원
for i in arr:
  cnt+=1 
  if cnt >= i:
    result+=1
    cnt = 0
print(result)


    
