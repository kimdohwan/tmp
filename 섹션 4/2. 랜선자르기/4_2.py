from algorithm.al_read import read_file


def count(len, lines):
    cnt = 0
    for x in lines:
        cnt += (x // len)
    return cnt


def b(n, lines):
    res = 0
    largest = max(lines)
    lt = 1
    rt = largest
    while lt <= rt:
        mid = (lt + rt) // 2
        if count(mid, lines) >= n:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1
    return res


if __name__ == '__main__':
    for i, o in read_file(4, 2):
        print('----------------')

        me = b(
            int(i[0].split(' ')[1]),
            list(map(lambda x: int(x), i[1:]))
        )

        answer = int(o[0])
        print(me == answer)
        print('\n', me, '\n', answer)
