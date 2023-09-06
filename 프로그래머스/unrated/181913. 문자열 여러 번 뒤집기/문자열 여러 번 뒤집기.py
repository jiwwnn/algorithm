def solution(my_string, queries):
    for i in queries:
        s,e = i[0], i[1]
        my_string = my_string[:s] + ''.join(reversed(my_string[s:e+1])) + my_string[e+1:]
    return my_string