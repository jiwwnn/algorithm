def solution(a, b, c, d):
    answer = 0
    
    lst = [a, b, c, d]
    lst.sort()
    print(lst)
    if lst[0] == lst[3]:
        answer = 1111*lst[0]
    elif lst[0] == lst[2]:
        answer = (10 * lst[0] + lst[3])**2    
    elif lst[1] == lst[3]:
        answer = (10 * lst[1] + lst[0])**2  
    elif lst[0] == lst[1] and lst[2] == lst[3]:
        answer = (lst[0] + lst[2]) * abs(lst[0] - lst[2])
    elif lst[0] == lst[1]:
        answer = lst[2] * lst[3]
    elif lst[1] == lst[2]:
        answer = lst[0] * lst[3]
    elif lst[2] == lst[3]:
        answer = lst[0] * lst[1]
    else:
        answer = lst[0]
    print(lst[0], lst[2], answer, (lst[0] + lst[2]) * abs(lst[0] - lst[2]))
    return answer