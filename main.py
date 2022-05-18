def next_bigger(n):
    cap = int(''.join(sorted(str(n), reverse=True)))
    if n == cap:
        return -1
    f = sorted(str(n))
    for c in range(n+1, cap+1):
        if sorted(str(c)) == f:
            return c
