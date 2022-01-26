'''
모든 도시의 쌍 (a,b)에 대해서 a에서 b로 가는데 필요한 비용의 최솟값을 출력하기
플로이드 알고리즘
'''
# d(x,y) = min ( d(x,y) , d(x,k)+ d(k,y) )
# a 도시에서 b 도시로 가는데 여러 경로가 있을 수 있음.
# 최소 비용을 구하는 문제이므로 이미 저장되어 있는 값보다 더 큰 값이 들어온다면 
# 무시해주기

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
gr =[ [INF]*(n) for i in range(n)]
for i in range(m):
	a,b,c = map (int, input().split())
	gr[a-1][b-1] = min(c,gr[a-1][b-1])
for i in range(n):
	gr[i][i]=0

for k in range(n):
	for i in range(n):
		for j in range(n):
			gr[i][j]=min (gr[i][j],gr[i][k]+gr[k][j])

for i in range(n):
	for j in range(n):
		if gr[i][j]==INF:
			print(0, end= ' ')
		else:
			print(gr[i][j], end = ' ')
	print()	
