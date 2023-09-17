def solution(arr):
    for i in arr:
        if len(arr) < len(i):
            arr.append([0]*len(i))
        elif len(arr) > len(i):
            i += [0]*(len(arr)-len(i))
    return arr