def solution(a, b, n):
    free = 0
    
    while n>0:
        free += n//a*b
        n = (n//a)*b + n%a
        
        if n < a:
            break
    return free