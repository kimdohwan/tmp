from algorithm.al_read import read_file


def b(li):
    print(li)

    tmp = []
    for i, value in enumerate(li[::-1]):
        tmp.insert(value, len(li) - i)
    return tmp


if __name__ == '__main__':
    for i, o in read_file(4, 10):
        print('----------------')

        me = b(
            [list(map(lambda a: int(a), i.split(' '))) for i in i[1:]][0],
        )

        answer = [int(s) for s in o[0].split(' ')]
        print(me == answer)
        print('\nme', me, '\nanswer', answer)