from algorithm.al_read import read_file


def a(li):
    print(li)
    cnt = 0

    last_idx = len(li) - 1
    for i, lli in enumerate(li):
        for j, lli_val in enumerate(lli):
            if i == 0:
                up = 0
            else:
                up = li[i - 1][j]

            if i == last_idx:
                down = 0
            else:
                down = li[i + 1][j]

            if j == 0:
                left = 0
            else:
                left = lli[j - 1]

            if j == last_idx:
                right = 0
            else:
                right = lli[j + 1]

            if up < lli_val and down < lli_val and right < lli_val and left < lli_val:
                cnt += 1
    return cnt


if __name__ == '__main__':
    for i, o in read_file(3, 9):
        print('----------------')
        iiii = list(map(lambda li: [int(iii) for iii in li], (ii.split(' ') for ii in i[1:int(i[0]) + 1])))

        me = a(iiii)
        answer = int(o[0])
        print(me == answer)
        print(me, '\n', answer)
