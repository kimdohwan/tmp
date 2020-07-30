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
        # yield a
        yield lines[0]


def a(string):
    print(string)
    n = int(''.join(filter(lambda s: s.isdigit(), string)))
    b = 0
    for i in range(1, n + 1):
        if n % i == 0:
            b += 1

    print(n)
    print(b)


if __name__ == '__main__':
    for i in get_input():
        print(a(i))