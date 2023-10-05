n = int(input())

towers = []
lst = list(map(int,input().split(" ")))
result = [0 for _ in range(n)]
m_height = 0
m_height_num = 0


for i in range(n):
    height = lst[i]
    if i == 0:
        towers.append(lst[i])
        result[i] = 0
        
        m_height = height
        m_height_num = i+1

    
    if i != 0 and towers[-1] < height:
        if m_height >= height:
            towers.append(height)
            
            result[i] = m_height_num
            m_height = height
            m_height_num = i+1
        else:
            m_height = height
            m_height_num = i+1
            towers.append(lst[i])
            result[i] = 0
    else:
        if i == 0:
            continue
        else:
            towers.append(height)
            result[i] = m_height_num

print(' '.join(map(str,result)))