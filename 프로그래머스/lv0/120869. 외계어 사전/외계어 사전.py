from itertools import permutations

def solution(spell, dic):
    lst = []
    for i in permutations(spell, len(spell)):
        lst.append(''.join(i))
    
    for word in dic:
        if word in lst:
            return 1
    return 2