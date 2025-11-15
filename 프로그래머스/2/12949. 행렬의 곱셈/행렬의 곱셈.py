def solution(arr1, arr2):
    n = len(arr1)          # arr1의 행 개수
    m = len(arr1[0])       # arr1의 열 개수 = arr2의 행 개수
    k = len(arr2[0])       # arr2의 열 개수

    # 결과 행렬을 0으로 초기화 (n x k)
    answer = [[0] * k for _ in range(n)]

    # 행렬 곱셈
    for i in range(n):           # arr1의 i번째 행
        for j in range(k):       # arr2의 j번째 열
            for t in range(m):   # 공통 차원
                answer[i][j] += arr1[i][t] * arr2[t][j]

    return answer
