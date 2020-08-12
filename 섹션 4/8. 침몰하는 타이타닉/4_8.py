from algorithm.al_read import read_file


def b(*args):
    # print(args)
    max_weight, li = args
    answer = 0

    # li.sort()
    # while li:
    #     p_weight = li.pop(0)
    #     partner_max_weight = max_weight - p_weight
    #
    #     min_diff = partner_max_weight
    #     partner_idx = len(li)
    #     for i in range(len(li)):
    #         diff = partner_max_weight - li[i]
    #
    #         if diff == 0:
    #             partner_idx = i
    #             break
    #         elif 1 < diff < min_diff:
    #             min_diff = diff
    #             partner_idx = i
    #
    #     if partner_idx == len(li):
    #         answer += len(li) + 1
    #         break
    #     else:
    #         li.pop(partner_idx)
    #         answer += 1

    li.sort()
    print(li)
    s = 0
    e = len(li) - 1
    while True:
        solo = (li[s] + li[e]) > max_weight

        if solo:
            e -= 1
        else:
            s += 1
            e -= 1

        answer += 1

        if s >= e:
            if s == e:
                answer += 1
            break

    return answer


if __name__ == '__main__':
    for i, o in read_file(4, 8):
        print('----------------')

        me = b(
            int(i[0].split(' ')[1]),
            [list(map(lambda a: int(a), i.split(' '))) for i in i[1:]][0],
        )

        answer = int(o[0])
        print('\nme', me, '\nanswer', answer)
        print(me == answer)
