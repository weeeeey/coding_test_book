'''
n*m인 그래프에서 1열부터 시작해서 한 열당 한 곳을 지정해서 다음 열로 이동할때, m열까지 이동했을경우
가장 많이 금광을 얻을 수 있는 양은?
ex) 1,2 에서 출발하면 (2,1)(2,2)(2,3) 중 한 곳으로 이동 가능 
'''
# 항상 최대의 수를 구한다면 그것이 정답이 되므로 점화식 a[i][j] = a[i][j[]+ max(a[i-1][j-1],a[i][j-1],a[i+1][j-1]) 을
#코딩으로 구현하면 된다.
# 한줄 리스트를 이중 배열로 변환하기
# 점화식을 위해서 첫 열과 끝 열에 [0]*m을 추가해주기
# 한열씩 앞으로 전진하므로 이중 for문에서 행이 안으로

n, m = map(int,input().split())
arr = list(map(int,input().split()))
gr = [[0]*m for i in range(n)]
for i in range(n*m):
  gr[i//m][int(i%m)] = arr[i]
gr.append([0]*m)
gr.insert(0,[0]*m)

for j in range(1,m):
  for i in range(1,n+1):
    gr[i][j] = gr[i][j] + max(gr[i-1][j-1],gr[i][j-1],gr[i+1][j-1])
result = 0
for i in range(1,n+1):
  if gr[i][m-1] > result:
    result = gr[i][m-1]
print(result)
