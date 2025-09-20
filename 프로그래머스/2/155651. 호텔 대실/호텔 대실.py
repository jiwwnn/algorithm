import heapq

def to_minutes(time_str):
    # "HH:MM" → 분 단위 정수 변환
    h, m = map(int, time_str.split(":"))
    return h * 60 + m

def solution(book_time):
    # 1. 시간 변환 + 퇴실시간 + 10분 반영
    times = []
    for start, end in book_time:
        times.append((to_minutes(start), to_minutes(end) + 10))

    # 2. 시작 시간 기준 정렬
    times.sort() # cf.각 튜플의 0번 인덱스 우선 비교, 0번 인덱스 값 같을 시 1번 인덱스 고려

    # 3. 최소 힙 준비
    heap = []

    # 4. 예약 순회
    for start, end in times:
        if heap and heap[0] <= start: # heap 최소값과 start 비교
            heapq.heappop(heap) # heapq 모듈 항상 내부적으로 0번 인덱스(최소값) pop
        heapq.heappush(heap, end) # 대상리스트와 값 둘 다 넘겨줘야 함

    # 5. 필요한 방의 개수 = 힙의 최대 길이
    return len(heap)

