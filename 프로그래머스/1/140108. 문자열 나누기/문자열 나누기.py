def solution(s):
    count = 0
    dic = {}

    for i, j in enumerate(s):        
        if j not in dic:
            dic[j] = 1
        else:
            dic[j] += 1
            
        val = list(dic.values())
        if len(val) >= 2 and len(set(val)) == 1:
            count += 1
            dic = {}
            s = s[i+1:]
            
        if i == len(s)-1:
            count += 1

    return count

def solution(s):
    count = 0
    i = 0

    while i < len(s):
        x = s[i]
        x_count = 0
        other_count = 0

        for j in range(i, len(s)):
            if s[j] == x:
                x_count += 1
            else:
                other_count += 1

            if x_count == other_count:
                count += 1
                i = j + 1  # 다음 분리 시작점으로 이동
                break
        else:
            # 끝까지 가도 개수가 같아지지 않으면 남은 부분 하나로 분리
            count += 1
            break

    return count
