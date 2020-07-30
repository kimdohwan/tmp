from algorithm.al_read import read_file


def reverse(x):
    return int((''.join(str(x)[::-1])))


def is_prime(x):
    for i in range(2, x):
        if (x % i) == 0:
            return False
    return True


if __name__ == '__main__':
    for i, v in read_file(2, 8):
        li = []
        for ii in [int(s) for s in i[1].split()]:
            r = reverse(ii)
            if r == 1:
                continue
            if is_prime(r):
                li.append(r)
        print(li, '\n', v)
