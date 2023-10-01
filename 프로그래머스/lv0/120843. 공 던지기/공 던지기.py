def solution(numbers, k):
    idx = 1
    # k번째 던지는 사람 = k-1번째 사람이 토스한 상대
    for i in range(k-1):
        # 두 칸씩 이동하므로 for문 2번 돌리기
        for j in range(2):
            idx += 1
            # len(numbers)보다 클 시 -len(numbers)하여 맨 앞 인덱스로 돌아가기
            if idx > len(numbers):
                idx -= len(numbers)
    return idx 

