'''
각각의 음식의 갯수가 적힌 리스트가 주어졌을때 1초에 한개씩 먹을 수 있다고 가정.
이때 k초에 오류가 생긴다.
이 오류를 고친 후 다시 먹을 수 있는 음식의 번호는?
단, 더 섭취할 음식이 없다면 -1을 출력
'''
# 그리드가 아닌 단순하게 풀어봄
# k초 만큼 리스트를 할당한 후 시간이 흐르면서 먹게 되는 음식의 번호를 시간 리스트에 할당하는 방식
# [시간 초과가 뜨는 코드]
# k가 2백만 이하길래 요렇게 풀었는데 효율성 테스트 제한은 k가 20조까지 주어짐
# O(n)으로는 시간제한 뜸

k = int(input())
food_times = list(map(int,input().split()))

arr = [-1]*(k+2)
arr[0] = 0
temp = 0
s = sum(food_times)
for i in range(1,k+2):
    if i > s :
        arr[i] = -1
        break
    if food_times[temp%3] != 0:
        arr[i] = temp%3
        food_times[temp%3]-=1
        temp = (temp+1)%3
        
    else:
        while(food_times[temp%3] == 0):
            temp = (temp + 1)%3 
        arr[i] = temp%3
        food_times[temp%3] -=1
        temp = (temp+1)%3
print((arr[k+1]+1))

# [그리디 형식으로 푼 방식]
# 우선순위 큐를 이용하여 푼다. 

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
    s_t = 0 
    p_t = 0
    l = len(food_times)
    
    while ( s_t + l*((q[0][0])-p_t)) <= k:
        now = heapq.heappop(q)[0]
        s_t += (now-p_t)*l
        l -= 1
        p_t = now
    result = sorted(q, key = lambda x:x[1])
    return result[(k-s_t)%l][1]



















