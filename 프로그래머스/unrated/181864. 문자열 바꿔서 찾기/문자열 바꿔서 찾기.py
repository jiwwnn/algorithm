def solution(myString, pat):
    myString = myString.replace('A', '_').replace('B', 'A').replace('_', 'B')
    return int(pat in myString)