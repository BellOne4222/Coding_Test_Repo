def solution(n,a,b):
    Red = min(a,b) # 대전 왼쪽 선수
    Blue = max(a,b) # 대전 오른쪽 선수

    round = 1 # 1라운드 부터 시작
    
    while True:
        # 1번↔2번, 3번↔4번, ... , N-1번↔N번의 참가자끼리 게임을 진행합니다.
        # Red, Blue가 매치 상대가 되기까지의 경우의 수를 나타내므로 서로 상대가 되면 break
        # Blue는 무조건 짝수여야하고, Red와 Blue는 무조건 1 차이가 나야 대전 상대가 된다.
        if Blue % 2 == 0 and Blue - Red == 1:
            break
        
        # 다음 라운드에서의 각각의 번호는 원래 번호에서 2만큼 나눈 값인데, 선수의 번호는 1부터 시작하므로 1 더해주기
        Red = (Red+1) // 2 
        Blue = (Blue+1) // 2
        round += 1

    return round

# 궁금증 : 0.5도 넣어서 돌려봤는데 안되서 이유를 생각해보니 0.5를 더하면 정수로 변환하는 과정에서 소수점 이하가 버려지기 때문에