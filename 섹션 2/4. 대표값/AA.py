from math import ceil

if __name__ == '__main__':
    a, b = 15, [12, 34, 17, 6, 11, 15, 27, 42, 39, 31, 25, 36, 35, 25, 17, ]

    # avg = ceil(sum(b) / len(b))
    avg = round(sum(b) / len(b))

    a = [None, 9999999]
    for num, s in enumerate(b):
        t = abs(avg - s)
        if t < a[1]:
            a[0] = num + 1
            a[1] = s
        elif t == a[1]:
            if s < a[1]:
                a[0] = num + 1
                a[1] = s

    print(a)


n, a = 15, [12, 34, 17, 6, 11, 15, 27, 42, 39, 31, 25, 36, 35, 25, 17, ]
ave = sum(a) / n
ave = ave + 0.5
ave = int(ave)
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)
