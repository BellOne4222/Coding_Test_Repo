# 1. 창구수 설정
# 2. 고객 별로 대기 번호를 받은 시각과 상담에 걸리는 시간을 설정
# 3. 생성된 데이터를 이용해 상담 처리 과정을 시뮬레이션
# if len(상담창구) == 0: 즉시 상담
# not 빈 창구 : wait
# end 상담시간 -> 빈창구 +=1
# 전체 고객의 대기시간 합?

N = 2
data = [[0, 3], [2, 5], [4, 2], [5, 3]]

changgu = [[] for _ in range(N)]
print(changgu)