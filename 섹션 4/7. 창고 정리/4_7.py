from algorithm.al_read import read_file


def b(li):
    li, n = li[0], int(li[1][0])
    print(li, n)
    answer = 0

    li.sort()
    for _ in range(n):
        li[0] += 1
        li[-1] -= 1
        li.sort()
    answer = li[-1] - li[0]

    return answer


if __name__ == '__main__':
    for i, o in read_file(4, 7):
        print('----------------')

        me = b(
            [list(map(lambda a: int(a), i.split(' '))) for i in i[1:]],
        )

        answer = int(o[0])
        print(me == answer)
        print('\nme', me, '\nanswer', answer)