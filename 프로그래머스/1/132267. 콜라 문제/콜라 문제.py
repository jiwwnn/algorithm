def solution(a, b, n):
    free = 0
    
    while n>0:
        free += n//a*b
        n = n//a*b + n%a # 새로 얻은 콜라 + 남은 병
        
        if n < a:
            break
    return free