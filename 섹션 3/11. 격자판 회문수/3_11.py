from algorithm.al_read import read_file


def a(li):
    print(li)

    cnt = 0
    loop_num = (len(li) - 5) + 1
    for i in range(7):
        for j in range(loop_num):
            lli = li[i][j:j + 5]
            if lli[0] == lli[-1] and lli[1] == lli[-2]:
                cnt += 1

        vertical_li = [li[j][i] for j in range(7)]
        for j in range(loop_num):
            lli = vertical_li[j:j + 5]
            if lli[0] == lli[-1] and lli[1] == lli[-2]:
                cnt += 1

    return cnt


if __name__ == '__main__':
    for i, o in read_file(3, 11):
        print('----------------')
        iiii = list(map(lambda li: [int(iii) for iii in li], (ii.split(' ') for ii in i[0:9])))

        me = a(iiii)
        answer = o[0]
        print(me == int(answer))
        print('\n', me, '\n', answer)
