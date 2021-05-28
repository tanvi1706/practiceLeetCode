def canConstruct(self, s: str, k: int):
    n = len(s)
    if n == k:
        return True
    if n < k:
        return False
    from collections import Counter
    count = Counter(s)
    even = 0
    odd = 0
    for x,v in count.items():
        if v % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd > k:
        return False
    return True


