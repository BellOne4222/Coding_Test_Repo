def solution(video_len, pos, op_start, op_end, commands):
    # 시간 문자열을 초로 변환하는 함수
    def time_to_seconds(time_str):
        mm, ss = map(int, time_str.split(':'))
        return mm * 60 + ss
    
    # 초를 시간 문자열로 변환하는 함수
    def seconds_to_time(seconds):
        mm = seconds // 60
        ss = seconds % 60
        return f"{mm:02d}:{ss:02d}"
    
    # 오프닝 구간 체크 및 건너뛰기
    def skip_opening(current):
        if op_start_sec <= current <= op_end_sec:
            return op_end_sec
        return current
    
    # 초 단위로 변환
    video_len_sec = time_to_seconds(video_len)
    current_pos = time_to_seconds(pos)
    op_start_sec = time_to_seconds(op_start)
    op_end_sec = time_to_seconds(op_end)
    
    # 시작 시 오프닝 구간 체크
    current_pos = skip_opening(current_pos)
    
    # 명령 처리
    for command in commands:
        if command == "prev":
            # 10초 전으로 이동
            current_pos = max(0, current_pos - 10)
        elif command == "next":
            # 10초 후로 이동
            current_pos = min(video_len_sec, current_pos + 10)
        
        # 명령 실행 후 오프닝 구간 체크
        current_pos = skip_opening(current_pos)
    
    # 결과를 "mm:ss" 형식으로 변환
    answer = seconds_to_time(current_pos)
    return answer