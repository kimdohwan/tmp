from functools import reduce

from algorithm.al_read import read_file


def a(li):
    print(li)

    total = 0
    middle_idx = len(li) // 2
    for i, lli in enumerate(li):
        if i <= middle_idx:
            total += reduce(lambda a, b: a + b, lli[middle_idx - i: middle_idx + 1 + i])
        else:
            total += reduce(lambda a, b: a + b, lli[i - middle_idx: -(i - middle_idx)])

    return total


if __name__ == '__main__':
    for i, o in read_file(3, 7):
        iiii = list(map(lambda li: [int(iii) for iii in li], (ii.split(' ') for ii in i[1:])))
        me = a(iiii)
        answer = int(o[0])
        print(me == answer)
        print(me, '\n', answer)
