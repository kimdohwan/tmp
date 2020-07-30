if __name__ == '__main__':
    n, k = 1000, 12

    li = []
    for i in range(1, n + 1):
        if n % i == 0:
            li.append(i)

    if len(li) < k:
        print(-1)
    else:
        print(li[k - 1])
    pass