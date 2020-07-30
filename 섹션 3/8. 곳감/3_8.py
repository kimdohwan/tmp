from functools import reduce

from algorithm.al_read import read_file


def a(two_two, rot_input_li):
    print(two_two)
    print(rot_input_li)

    rotated = [[i for i in li] for li in two_two]
    for input_val in rot_input_li:
        a, direction, jump = input_val
        jump_n = jump % len(two_two)
        for i in range(len(two_two)):
            if direction == 1:
                moved = i + jump_n
                if moved >= len(two_two):
                    moved -= (len(two_two) - 1)
                rotated[a - 1][i] = two_two[a - 1][moved]
            else:
                rotated[a - 1][i] = two_two[a - 1][i - jump_n]

    total = 0
    # mid = len(rotated) // 2
    for i, li in enumerate(rotated):
        for j in li[i: -i + 1]:
            total += j

    return total


def answer():
    n=int(input())
    a=[list(map(int, input().split())) for _ in range(n)]
    m=int(input())
    for i in range(m):
        h, t, k=map(int, input().split())
        if(t==0):
            for _ in range(k):
                a[h-1].append(a[h-1].pop(0))
        else:
            for _ in range(k):
                a[h-1].insert(0, a[h-1].pop())

    res=0
    s=0
    e=n-1
    for i in range(n):
        for j in range(s, e+1):
            res+=a[i][j]
        if i<n//2:
            s+=1
            e-=1
        else:
            s-=1
            e+=1
    return res


if __name__ == '__main__':
    for i, o in read_file(3, 8):
        print('----------------')
        iiii = list(map(lambda li: [int(iii) for iii in li], (ii.split(' ') for ii in i[1:int(i[0]) + 1])))
        j = list(map(lambda li: [int(jjj) for jjj in li], (j.split(' ') for j in i[int(i[0]) + 2:])))

        me = a(iiii, j)
        answer = int(o[0])
        print(me == answer)
        print(me, '\n', answer)
