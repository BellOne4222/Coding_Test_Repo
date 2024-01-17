# 반례 : [["05:57", "06:02"], ["04:00", "06:59"], ["03:56", "07:57"], ["06:12", "08:55"], ["07:09", "07:11"]]

def solution(book_time):
    # 예약 시각을 정렬
    book_time.sort() 
    # [['14:10', '19:20'], ['14:20', '15:20'], ['15:00', '17:00'], ['16:40', '18:20'], ['18:20', '21:20']]

    booking = []

    for i in range(len(book_time)):
        end_time = book_time[i][1]
        end_time_hour, end_time_min = end_time.split(":")
        end_time_min = int(end_time_min)
        end_time_min += 10

        # 처리한 시간이 60분을 넘어가면 시간을 올리고 분을 조정
        if end_time_min >= 60:
            end_time_hour = int(end_time_hour)
            end_time_hour += 1
            end_time_hour = str(end_time_hour).zfill(2)
            end_time_min -= 60
            end_time_min = str(end_time_min).zfill(2)
        else:
            end_time_min = str(end_time_min).zfill(2)

        cleaning_time = end_time_hour + ":" + end_time_min  # 청소 종료 시각

        if booking:
            # 만약 현재 예약 시간이 다음 예약 시작 시간보다 늦다면
            # 기존 예약을 삭제하고 현재 예약을 추가
            if booking[0] > book_time[i][0]:
                booking.append(cleaning_time)
            else:
                booking.pop(0)
                booking.append(cleaning_time)
            booking.sort()
        else:
            booking.append(cleaning_time)

    return len(booking)