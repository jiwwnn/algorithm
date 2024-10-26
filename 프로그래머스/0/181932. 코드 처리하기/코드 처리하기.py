def solution(code):
    ret = ''
    mode = 0 
    next_mode = 0
    
    for idx, value in enumerate(code):
        if mode == 0:
            if value != '1' and idx % 2 == 0 :
                ret += value
            elif value == '1':
                next_mode = 1
            
        if mode == 1:
            if value != '1' and idx % 2 != 0:
                ret += value
            elif value == '1':
                next_mode = 0
                
        mode = next_mode
        
    if len(ret) == 0:
        return 'EMPTY'
    return ret