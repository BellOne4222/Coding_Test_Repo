def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i] = [sizes[i][1],sizes[i][0]]
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
    
    return max(w) * max(h)            
    
    