def solution(n, l, r):
    return count_ones(n, l, r)

def count_ones(n, l, r):
    if n == 0:
        return 1 if l == 1 and r == 1 else 0

    count = 0
    length = 5 ** n
    part = length // 5

    for i in range(5):
        start = i * part + 1
        end = (i + 1) * part

        if r < start or l > end:
            continue
        if i == 2:
            continue

        l2 = max(l, start) - start + 1
        r2 = min(r, end) - start + 1

        count += count_ones(n-1, l2, r2)

    return count
