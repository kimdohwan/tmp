import os
import re
import sys
from os.path import join, dirname


def get_dir_name(path, exp):
    dir_p = re.compile(exp)
    for d in os.listdir(path):
        if bool(dir_p.match(d)):
            return d


def in_and_out(path_ex, ex_dir_list):
    dic = {
        'in': {},
        'out': {},
    }
    for f in ex_dir_list:
        try:
            in_out = re.search('(in|out)(\d+)\.txt', f)
            in_or_out, order_num = in_out.group(1), int(in_out.group(2))
        except Exception:
            continue

        with open(join('', join(path_ex, f))) as ff:
            lines = []
            for l in ff.readlines():
                lines.append(l.rstrip())

            # lines = [l.decode().rstrip() for l in ff.readlines()]

            dic[in_or_out][order_num] = lines
    return dic


def read_file(section_num=None, ex_num=None):
    d_section = get_dir_name(dirname(__file__), f'\w+ {section_num}')
    d_ex = get_dir_name(join(dirname(__file__), d_section), f'{ex_num}\. \w+')

    path_ex = join(join(dirname(__file__), d_section), d_ex)
    file_list = os.listdir(path_ex)

    result = in_and_out(path_ex, file_list)

    n = 1
    while True:
        try:
            i, o = result['in'][n], result['out'][n]
            yield i, o
        except Exception:
            break
        n += 1

    pass

    # section_num = 2
    # dir_p = re.compile(f'\w+ {section_num}')
    # for d in os.listdir('.'):
    #     if bool(dir_p.match(d)):
    #         dir_name = d
    #
    # ex_num = 2
    # dir_p = re.compile(f'{ex_num}\. \w+')
    # for d in os.listdir(f'./{dir_name}'):
    #     if bool(dir_p.match(d)):
    #         print(d)


if __name__ == '__main__':
    a = [i for i in read_file(2, 2)]
    pass
