def next_higher_same_ones(n):
    c = n
    c0 = c1 = 0
    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c >>= 1
    while (c & 1) == 1:
        c1 += 1
        c >>= 1
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1
    pos = c0 + c1
    n |= (1 << pos)
    n &= ~((1 << pos) - 1)
    n |= (1 << (c1 - 1)) - 1
    return n

# Test Case
n = 78  # binary: 1001110
print("Next Higher with Same 1s:", next_higher_same_ones(n))
