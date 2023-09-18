def solution(arr, n):
    for i in range(len(arr)%2, len(arr)+1, 2):
        if i > 0:
            arr[i-1] += n  
    return arr