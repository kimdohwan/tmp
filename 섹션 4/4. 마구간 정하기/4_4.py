from al_read import read_file


def a(n, li):
    print(n, li)

    li.sort()

    max_dis = 0
    for i in range(1, li[-1]):
        cnt = 1
        prev_j = 0
        for j in range(1, len(li)):
            if li[j] - li[prev_j] >= i:
                prev_j = j
                cnt += 1
            if n < cnt:
                break
        if n <= cnt:
            max_dis = i
        elif cnt < n:
            break

    return max_dis


if __name__ == '__main__':
    for _input, output in read_file(4, 4):
        print('-------------------------------------')
        me = a(
            int(_input[0].split(' ')[1]),
            [int(ii) for ii in _input[1:]],
        )
        ans = int(output[0])

        print('m', me)
        print(ans)
        print(ans == me)
