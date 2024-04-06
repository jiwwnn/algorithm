def solution(arr):
    answer = []
    if 2 in arr:
        start = arr.index(2)
        arr_r = list(reversed(arr))
        end = len(arr_r) - arr_r.index(2)
        answer = arr[start:end]
    
    if 2 not in arr:
        answer.append(-1)
    
    return answer