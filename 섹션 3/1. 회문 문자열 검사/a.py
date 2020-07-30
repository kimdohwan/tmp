from os.path import dirname, join


def get_input():
    for i in range(1, 6):
        path = join(dirname(__file__), f'in{i}.txt')
        with open(path, 'r') as f:
            lines = f.readlines()

        # a = []
        # for lili in [i.strip().split(' ') for i in lines[1:]]:
        #     li = []
        #     for s in lili:
        #         try:
        #             li.append(int(s))
        #         except ValueError:
        #             pass
        #     if li:
        #         a.append(li)
        yield [s.strip() for s in lines[1:]]


def a(aa):
    print('-------------')
    for string in aa:
        split_idx = (len(string) // 2)
        for i in range(split_idx):
            nomal_idx = i
            reverse_idx = - (i + 1)
            if string[nomal_idx].lower() == string[reverse_idx].lower():
                pass
            else:
                print('NO')
                break
        else:
            print('YES')


if __name__ == '__main__':
    for i in get_input():
        a(i)
