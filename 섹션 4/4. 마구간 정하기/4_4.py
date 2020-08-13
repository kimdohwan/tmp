from al_read import read_file

aaa = 0
bbb = 0


def a(n, li):
    global aaa
    print(n, li)

    li.sort()
    max_dis = 0
    for i in range(1, li[-1]):
        cnt = 1
        prev_j = 0
        aaa += 1
        for j in range(1, len(li)):
            aaa += 1
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


def aa(c, Line, n):
    global bbb

    def Count(len):
        global bbb
        cnt = 1
        ep = Line[0]
        for i in range(1, n):
            bbb += 1
            if Line[i] - ep >= len:
                cnt += 1
                ep = Line[i]
        return cnt

    Line.sort()
    lt = 1
    rt = Line[n - 1]
    while lt <= rt:
        bbb += 1
        mid = (lt + rt) // 2
        if Count(mid) >= c:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1

    return res


if __name__ == '__main__':
    for _input, output in read_file(4, 4):
        print('-------------------------------------')
        me = a(
            int(_input[0].split(' ')[1]),
            [int(ii) for ii in _input[1:]],
        )

        me = aa(
            int(_input[0].split(' ')[1]),
            [int(ii) for ii in _input[1:]],
            len([int(ii) for ii in _input[1:]])
        )
        ans = int(output[0])

        print('m', me)
        print(ans)
        print(ans == me)
        print(aaa)
        print(bbb)
