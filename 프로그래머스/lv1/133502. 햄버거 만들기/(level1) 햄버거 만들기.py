def solution(ingredient):
    hamburger = [1, 2, 3, 1]
    kitchen = []
    count = 0
    for i in ingredient:
        kitchen.append(i) # 스택에 하나씩 넣으면서 햄버거 배열과 같아지면 같은 4개 pop 처리해서 같을때마다 햄버거 개수 1개 늘리면서 개수 반환하는 방식
        if kitchen[-4:] == hamburger:
            count += 1
            for j in range(4):
                kitchen.pop()
    return count
        
        
        
    
    