from algorithm.al_read import read_file


def count(min_val, li):
    a = 0
    cnt = 0
    for i in li:
        tmp = a + i
        if tmp < min_val:
            a += i
        else:
            a = i
            cnt += 1
    return cnt


def b(n, li):
    print(n, li)

    min_val = sum(li) // n
    while True:
        if count(min_val, li) != n:
            return min_val - 1
        else:
            min_val += 1


if __name__ == '__main__':
    for i, o in read_file(4, 3):
        print('----------------')

        me = b(
            int(i[0].split(' ')[1]),
            list(map(lambda x: int(x), i[1].split(' ')))
        )

        answer = int(o[0])
        print(me == answer)
        print('\n', me, '\n', answer)
