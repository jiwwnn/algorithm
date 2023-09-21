def solution(my_string):
    lst = [(i,v.isupper()) for i, v in enumerate(my_string)]
    return ''.join([my_string[x[0]].lower() if x[1] == True else my_string[x[0]].upper() for x in lst])
