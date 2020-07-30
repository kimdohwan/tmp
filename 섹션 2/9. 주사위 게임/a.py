from os.path import join, dirname


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


def a(inp):
    max_money = 0
    for li in inp:
        li = [1, 2, 3, 4, 5, 6]

        bonus = 0
        multiple = 100

        set_li = set(li)
        if len(set_li) == len(li):
            pass
        elif len(set_li) == (len(li) - 1):
            bonus = 1000
            for i in set_li:
                li.remove(i)
        else:
            bonus = 10000
            multiple = 1000

        money = bonus + (multiple * max(li))
        # print(money)

        if max_money < money:
            max_money = money

    return max_money


if __name__ == '__main__':
    for inp in get_input():
        print(a(inp))
    pass
