from functools import reduce

from algorithm.al_read import read_file


def aa(input):
    m = 0
    max_var = None
    for string in (str(i) for i in input):
        cur_max = reduce(lambda x, y: int(x) + int(y), string)
        if m < cur_max:
            m, max_var = cur_max, int(string)

    return max_var


if __name__ == '__main__':
    for r in read_file(2, 6):
        input = [int(i) for i in r[0][1].split(' ')]
        print(aa(input), r[1])
