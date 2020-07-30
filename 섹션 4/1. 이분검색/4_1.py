from algorithm.al_read import read_file


def a(target, li):
    print(target, li)
    li.sort()

    s = 0
    e = len(li) - 1
    while True:
        mid = (s + e) // 2
        if li[mid] == target:
            return mid + 1
        elif li[mid] < target:
            s = mid + 1
        else:
            e = mid


if __name__ == '__main__':
    for i, o in read_file(4, 1):
        print('----------------')

        me = a(
            int(i[0].split(' ')[1]),
            list(map(lambda x: int(x), i[1].split(' ')))
        )
        answer = int(o[0])
        print(me == answer)
        print('\n', me, '\n', answer)
