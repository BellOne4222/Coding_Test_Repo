def solution(triangle):
    triangle = triangle[::-1]
    # 	[[4, 5, 2, 6, 5], [2, 7, 4, 4], [8, 1, 0], [3, 8], [7]]
    
    # 밑에서 부터 삼각형 한 줄씩 반복
    for i in range(len(triangle)):
        # 큰 삼각형 안에서 작은 삼각형으로 쪼개어서 하나씩 연산, 윗변의 값과 밑변의 2개의 값을 각각 더해주고 둘 중의 최대값으로 리스트 재구성해서 로직 반복 하여 삼각형 맨 위의 값을 출력
        for j in range(len(triangle[i])-1):
            triangle[i+1][j] = max((triangle[i][j] + triangle[i+1][j]) , (triangle[i][j+1] + triangle[i+1][j]))
    
    # 삼각형 맨 끝 값 반환
    return triangle[len(triangle)-1][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))