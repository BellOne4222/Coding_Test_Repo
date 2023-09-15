def solution(routes):
    routes.sort(key = lambda x:x[1]) # [[-20,-15],[-18,-13],[-14,-5],[-5,-3]]
    camera = 1
    
    standard = routes[0][1]
    
    for i in range(1,len(routes)):
        if routes[i][0] <= standard:
            pass
        else:
            camera += 1
            standard = routes[i][1]
    
    return camera
            
        
            
        