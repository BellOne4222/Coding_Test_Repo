# 이것이 취업을 위한 코딩테스트다 p.376 정수 삼각형

n = 5

triangle = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]

triangle = triangle[::-1]
dp_table = [[] for _ in range(n)]

dp_table[0] = triangle[0]
for i in range(1,n):
    for j in range(len(triangle[i])):
        dp_table[i].append(max(dp_table[i-1][j], dp_table[i-1][j+1]) + triangle[i][j])

print(dp_table[n-1][0])

