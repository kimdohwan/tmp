from os.path import dirname, join


def get_input():
    for i in range(1, 6):
        path = join(dirname(__file__), f'in{i}.txt')
        with open(path, 'r') as f:
            lines = f.readlines()

        a = []
        for lili in [i.strip().split(' ') for i in lines[1:]]:
            li = []
            for s in lili:
                try:
                    li.append(int(s))
                except ValueError:
                    pass
            if li:
                a.append(li)
        yield a


def aa(li):
    print(li)
    copy_li = li[:]
    for i, r in enumerate(li):
        if i == 0:
            continue
        if r and li[i - 1]:
            copy_li[i] = copy_li[i - 1] + 1

    return sum(copy_li)


if __name__ == '__main__':
    for i in get_input():
        print(aa(i[0]))
