def solution(my_string):
    answer = 0
    num_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in my_string:
        if i in num_lst:
            answer += int(i)
    return answer