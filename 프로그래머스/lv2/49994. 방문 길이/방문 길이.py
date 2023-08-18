def solution(dirs):
    start = (0,0)
    up = (0,1)
    down = (0,-1)
    left = (-1,0)
    right = (1,0)
    before = start
    check = []
    sm = 0
    road = 0
    cnt = 0
    
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            sm = tuple(sum(j) for j in zip(before, up))
            if sm[0] > 5 or sm[0] < -5 or sm[1] > 5 or sm[1] < -5:
                continue
            road = (before,sm)
            r_road = (sm,before)
            if road not in check:
                check.append(road)
                check.append(r_road)
                cnt += 1
            else:
                before = sm
                continue
            
            
        elif dirs[i] == 'D':
            sm = tuple(sum(j) for j in zip(before, down))
            if sm[0] > 5 or sm[0] < -5 or sm[1] > 5 or sm[1] < -5:
                continue
            road = (before,sm)
            r_road = (sm,before)
            if road not in check:
                check.append(road)
                check.append(r_road)
                cnt += 1
            else:
                before = sm
                continue
        elif dirs[i] == 'L':
            sm = tuple(sum(j) for j in zip(before, left))
            if sm[0] > 5 or sm[0] < -5 or sm[1] > 5 or sm[1] < -5:
                continue
            road = (before,sm)
            r_road = (sm,before)
            if road not in check:
                check.append(road)
                check.append(r_road)
                cnt += 1
            else:
                before = sm
                continue
        else:
            sm = tuple(sum(j) for j in zip(before, right))
            if sm[0] > 5 or sm[0] < -5 or sm[1] > 5 or sm[1] < -5:
                continue
            road = (before,sm)
            r_road = (sm,before)
            if road not in check:
                check.append(road)
                check.append(r_road)
                cnt += 1
            else:
                before = sm
                continue
                
        
        before = sm
        
    return cnt
        