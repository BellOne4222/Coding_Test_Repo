def solution(dots, lines):
    # 점과 선분을 오름차순으로 정렬
    dots.sort()
    lines.sort(reverse=True)
    
    covered = 0  # 덮인 점의 수
    segments_used = 0  # 사용된 선분의 수
    i = 0  # 점 배열의 인덱스
    
    # 모든 점이 덮힐 때까지 반복
    while covered < len(dots):
        segments_used += 1  # 선분 하나를 더 사용
        start = dots[i]  # 현재 덮을 점의 위치
        
        # 가장 긴 선분으로 가능한 많은 점을 덮기
        for line in lines:
            # 현재 위치에서 시작하여 선분으로 덮을 수 있는 가장 먼 점 찾기
            while i < len(dots) and dots[i] <= start + line:
                i += 1
            break
        
        # 덮인 점의 수 업데이트
        covered = i
        
    return segments_used

print(solution([1,3,4,6,7,10], [2,2,2,2]))