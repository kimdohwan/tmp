from algorithm.al_read import read_file


def a(li):
    print(li)

    for i in range(9):
        # 가로 list
        if len(set(li[i])) < 9:
            return 'NO'

        # 세로 list
        vertical_li = [li[j][i] for j in range(9)]
        if len(set(vertical_li)) < 9:
            return 'NO'

    # 3x3 list
    for ii in range(0, 9, 3):
        for jj in range(0, 9, 3):
            b = [li_hor[ii: ii + 3] for li_hor in li[jj: jj + 3]]
            bb = [kk for kkk in b for kk in kkk]
            if len(set(bb)) < 9:
                return 'NO'

    return 'YES'


if __name__ == '__main__':
    for i, o in read_file(3, 10):
        print('----------------')
        iiii = list(map(lambda li: [int(iii) for iii in li], (ii.split(' ') for ii in i[0:9])))

        me = a(iiii)
        answer = o[0]
        print(me == answer)
        print('\n', me, '\n', answer)
