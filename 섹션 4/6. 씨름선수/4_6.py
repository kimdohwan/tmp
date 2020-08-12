from algorithm.al_read import read_file


def b(li):
    print(li)
    answer = len(li)
    for i, (height, weight) in enumerate(li):
        tmp = li[:]
        tmp.pop(i)
        for p_height, p_weight in tmp:
            min_height = min(height, p_height)
            min_weight = min(weight, p_weight)
            if height == min_height and weight == min_weight:
                answer -= 1
                break

    return answer

# while 문으로 돌려서
# 2중 for loop의 값도 비교 후
# i += 1 해주는 방식으로 하면
# for를 덜돌고 리스트를 만들지 않아도 될듯


if __name__ == '__main__':
    for i, o in read_file(4, 6):
        print('----------------')

        me = b(
            [list(map(lambda a: int(a), i.split(' '))) for i in i[1:]]
        )

        answer = int(o[0])
        print(me == answer)
        print('\nme', me, '\nanswer', answer)