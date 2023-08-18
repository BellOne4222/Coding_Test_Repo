# 개미 군단

def solution(hp):
    general = hp // 5 # 장군개미 수
    soldier = (hp-(5*general))//3 # 병정개미 수는 전체에서 장군개미수 빼고 난 수
    normal = (hp-(5*general)-(3*soldier))//1 # 마지막 다 빼고 남은 일개미수
    answer = general+soldier+normal #업데이트 방식으로 풀어보기
    
    return answer