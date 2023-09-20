# def solution(s):
#     dic = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
#     for k, v in dic.items():
#         if k in s:
#             s = s.replace(k, str(v))
#     return int(s)


def solution(s):
    en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    dic = {k : v for k, v in zip(en, [i for i in range(10)]) }
    for k, v in dic.items():
        if k in s:
            s = s.replace(k, str(v))
    return int(s)
    