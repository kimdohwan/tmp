def aa(input):
    n = input
    ch = [0] * (n + 1)
    cnt = 0
    for i in range(2, n + 1):
        if ch[i] == 0:
            cnt += 1
            for j in range(i, n + 1, i):
                ch[j] = 1

    return cnt


if __name__ == '__main__':
    # for i in read_file(2, 7):
    #     print(i)

    a = [2, 200000, 150000, 90000, 100000]
    b = [1, 17984, 13848, 8713, 9592]
    for i, o in zip(a, b):
        print(aa(i), o)
