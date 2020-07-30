from functools import reduce

from algorithm.al_read import read_file


def a(li):
    print(li)

    # horizon
    max_sum = 0
    for hor in li:
        cur_sum = reduce(lambda a, b: a + b, hor)
        if max_sum < cur_sum:
            max_sum = cur_sum

    # vertical
    ver_li_list = list(map(lambda n: [hor_li[n] for hor_li in li], range(len(li))))
    for ver in ver_li_list:
        cur_sum = reduce(lambda a, b: a + b, ver)
        if max_sum < cur_sum:
            max_sum = cur_sum

    # cross
    left_sum = 0
    right_sum = 0
    n = len(li)
    for nn in range(n):
        left_sum += li[nn][nn]
        right_sum += li[nn][n - 1 - nn]
    if max_sum < left_sum:
        max_sum = left_sum
    elif max_sum < right_sum:
        max_sum = right_sum

    print(max_sum)


if __name__ == '__main__':
    for i, o in read_file(3, 6):
        iiii = list(map(lambda li: [int(iii) for iii in li], (ii.split(' ') for ii in i[1:])))
        a(iiii)

        print(int(o[0]))
