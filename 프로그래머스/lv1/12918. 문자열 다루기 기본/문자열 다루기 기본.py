def solution(s):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(s) == 4 or len(s) == 6:
        print(len(s))
        for i in s:
            if i not in num:
                return False
        return True
    return False

    
