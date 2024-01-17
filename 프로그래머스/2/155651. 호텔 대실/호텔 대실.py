def solution(book_time):
    
    book_time.sort()
    # [['14:10', '19:20'], ['14:20', '15:20'], ['15:00', '17:00'], ['16:40', '18:20'], ['18:20', '21:20']]
    
    booking = []
    
    for i in range(len(book_time)):
        end_time = book_time[i][1]
        end_time_hour, end_time_min = end_time.split(":")
        end_time_min = int(end_time_min)
        end_time_min += 10
        if end_time_min >= 60:
            end_time_hour = int(end_time_hour)
            end_time_hour += 1
            end_time_hour = str(end_time_hour)
            if len(end_time_hour) < 2:
                end_time_hour = end_time_hour.zfill(2)
            end_time_min -= 60
            
            end_time_min = str(end_time_min)
            if len(end_time_min) < 2:
                end_time_min = end_time_min.zfill(2)
        else:
            end_time_min = str(end_time_min)
        
        cleaning_time = end_time_hour + ":" + end_time_min # 19:30      
        
        if booking:
            if booking[0] > book_time[i][0]:
                booking.append(cleaning_time)
            else:
                booking.pop(0)
                booking.append(cleaning_time)
            booking.sort()
                
        else:
            booking.append(cleaning_time)
            
    return len(booking)
    
    