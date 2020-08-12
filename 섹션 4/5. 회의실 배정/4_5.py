from algorithm.al_read import read_file


def b(li):
    # print(li)
    li.sort(key=lambda i: i[1])

    tmp = []
    for i in range(len(li)):
        if i == 0:
            tmp.append(li[i])

        if tmp[-1][1] <= li[i][0]:
            tmp.append(li[i])

    return len(tmp)


if __name__ == '__main__':
    for i, o in read_file(4, 5):
        print('----------------')

        me = b(
            [list(map(lambda a: int(a), i.split(' '))) for i in i[1:]]
        )

        answer = int(o[0])
        print(me == answer)
        print('\n', me, '\n', answer)
