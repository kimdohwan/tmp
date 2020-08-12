from algorithm.al_read import read_file


def insert_smaller_value(s, e, li, string):
    if li[s] < li[e]:
        string += 'L'
        last_num = li[s]
        s += 1
    else:
        string += 'R'
        last_num = li[e]
        e -= 1

    return s, e, string, last_num


def insert_bigger_value(s, e, li, string):
    if li[s] > li[e]:
        string += 'L'
        last_num = li[s]
        s += 1
    else:
        string += 'R'
        last_num = li[e]
        e -= 1

    return s, e, string, last_num


def b(li):
    print(li)
    answer = 0

    s = 0
    e = len(li) - 1
    string = ''
    last_num = -1
    while True:
        if s == e and last_num < li[s]:
            string += 'L'
            break

        if max(last_num, li[s], li[e]) == last_num:
            break
        else:
            if min(last_num, li[s], li[e]) == last_num:
                s, e, string, last_num = insert_smaller_value(s, e, li, string)
            else:
                s, e, string, last_num = insert_bigger_value(s, e, li, string)

    return f'{len(string)} {string}'


if __name__ == '__main__':
    for i, o in read_file(4, 9):
        print('----------------')

        me = b(
            [list(map(lambda a: int(a), i.split(' '))) for i in i[1:]][0],
        )

        answer = ' '.join(o)
        print(me == answer)
        print('\nme', me, '\nanswer', answer)