if __name__ == '__main__':
    n, m = 8, 12
    a = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a.append(i + j)

    b = list(set(a))
    c = [0 for _ in range(len(b))]
    for n, i in enumerate(b):
        for j in a:
            if i == j:
                c[n] += 1

    max_n = max(c)
    for bb, cc in zip(b, c):
        if cc == max_n:
            print(bb, end=' ')

pass
