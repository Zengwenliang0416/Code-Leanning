def que2122():
    n = int(input())
    m = int(input())

    dic = {}
    """
    说明:计算输入数字的数位和
    ------------------------------------
    变量:i
    ------------------------------------
    返回:数位之和，eg. i = 10 return 1 + 0 = 1
    ------------------------------------
    """

    def sumnum(i):
        return sum(list(map(int, str(i))))

    for i in range(1, n + 1):
        dic[i] = sumnum(i)

    ordic = sorted(dic.items(), key=lambda x: x[1])
    print(ordic[m - 1][0])
    return 0


def que2117():
    #  55%
    n = int(input())
    h = list(map(int, input().split()))
    a = [[0 for j in range(1)] for i in range(len(h))]

    def cut(x):
        return int((x // 2 + 1) ** 0.5 // 1)

    count = 0
    for i in range(len(h)):
        while h[i] != 1:
            h[i] = cut(h[i])
            a[i].append(h[i])
            count += 1
    for i in range(n - 1):
        for j in range(min(len(a[i]), len(a[i + 1]))):
            if a[i][j] == 0:
                continue
            elif a[i][j] == a[i + 1][j]:
                if a[i][j] == 1 and a[i][j - 1] != 0:
                    continue
                count -= 1
    print(count)
    return 0


def que2380():
    n = input()
    idall = []
    for i in range(int(n)):
        time, id = input().split()
        idall.append(int(id))
    idall = list(set(idall))
    idall.sort()
    for i in range(len(idall)):
        print(idall[i])
    return 0


