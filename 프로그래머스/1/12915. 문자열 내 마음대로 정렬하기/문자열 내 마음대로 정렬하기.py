# def solution(strings, n):
#     strings.sort(key=lambda x: (x[n], x))
#     return strings

def solution(strings, n):
    print(f"\n입력 문자열 배열: {strings}")
    print(f"기준 인덱스 n: {n}")
    
    # 문자열을 (n번째 글자, 전체 문자열) 기준으로 정렬해주는 딕셔너리 생성
    # 키: n번째 글자
    # 값: 해당 글자를 가진 문자열들의 리스트
    dict_by_char = {}
    
    # 문자열을 n번째 글자로 분류
    for string in strings:
        char = string[n]
        if char in dict_by_char:
            dict_by_char[char].append(string)
        else:
            dict_by_char[char] = [string]
    
    print(f"\n문자열을 n번째 글자로 분류한 딕셔너리:")
    for char in dict_by_char:
        print(f"  '{char}': {dict_by_char[char]}")
    
    # 결과 리스트 준비
    result = []
    
    print("\n알파벳 순서대로 처리 및 각 그룹 내에서 사전순 정렬:")
    # 알파벳 순서대로 처리 ('a'부터 'z'까지)
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char in dict_by_char:
            print(f"  '{char}' 처리 중...")
            # 같은 n번째 글자를 가진 문자열들을 사전순으로 정렬
            strings_with_char = sorted(dict_by_char[char])
            print(f"    정렬 전: {dict_by_char[char]}")
            print(f"    정렬 후: {strings_with_char}")
            # 결과에 추가
            result.extend(strings_with_char)
            print(f"    현재까지 결과: {result}")
    
    print(f"\n최종 결과: {result}")
    return result