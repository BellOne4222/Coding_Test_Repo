import sys  # sys 모듈을 불러옵니다.

n = int(sys.stdin.readline())

meetings = []

for _ in range(n):
    meeting = list(map(int, sys.stdin.readline().split()))
    meetings.append(meeting)

standard = meetings[-1][0]

dp_table = [0] * (standard+1)

for i in reversed(range(len(meetings))):
    start, end, person = meetings[i][0], meetings[i][1], meetings[i][2]
    
    dp_table[start] += person
    
    idx = meetings.index(meetings[i])
    compare_lst = []
    for j in range(idx, len(meetings)):
        if meetings[j][0] >= end:
            if dp_table[start] < dp_table[start] + dp_table[meetings[j][0]]:
                compare_lst.append(dp_table[start] + dp_table[meetings[j][0]])
    if compare_lst:
        dp_table[start] = max(compare_lst)

print(max(dp_table))
            
        
        
        
        
        
            
            
        
    