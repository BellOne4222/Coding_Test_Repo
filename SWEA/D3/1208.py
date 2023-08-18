# 1208 Flatten  

tc = 10 
for test_case in range(1, tc + 1):
    T = int(input()) # dump 가능 횟수
    boxes = list(map(int, input().split())) 
    for i in range(T): 
        maxbox = max(boxes)
        minbox = min(boxes)
        # 최대 최소 값을 변경함에 따라 최소, 최댓값이 바뀔 수 있으므로 index를 구해서 해결
        minIndex = boxes.index(minbox) 
        maxIndex = boxes.index(maxbox) 
        boxes[minIndex] += 1 
        boxes[maxIndex] -= 1 
        if max(boxes) - min(boxes) < 2: # dump 가능 횟수 동안에 평탄화가 완료되면 반복 종료
            break
    answer = max(boxes) - min(boxes)  
    print("#{} {}".format(test_case, answer))



# 최댓값, 최솟값을 가진 위치를 찾는 과정에서 값을 변경함에 따라 최소, 최댓값이 바뀔 수 있으므로, index를 먼저 구해놓는다.


