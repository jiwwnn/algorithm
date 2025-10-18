def solution(s, skip, index):
    skip_set = set(skip)
    allowed = [chr(c) for c in range(ord('a'), ord('z') + 1) if chr(c) not in skip_set]
    pos = {ch: i for i, ch in enumerate(allowed)}
    L = len(allowed)
    step = index % L  # 큰 index 최적화

    out = []
    for ch in s:
        if ch in pos:
            out.append(allowed[(pos[ch] + step) % L])
    return "".join(out)