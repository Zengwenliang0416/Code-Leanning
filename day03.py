def que608():
    def is_primenumbers(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_prime(x):
        if (x == 2) or (x == 3):
            return True
        if (x % 6 != 1) and (x % 6 != 5):
            return False
        for i in range(5, int(x ** 0.5) + 1, 6):
            if (x % i == 0) or (x % (i + 2) == 0):
                return False
        print(x)
        return True

    pn = []
    n = 2
    while len(pn) != 2019:
        if is_prime(n):
            pn.append(n)
        n += 1

    return pn[2018]


print(que608())


def que():
    def is_prime(x):
        if x == 2 or x == 3:
            return True
        if x % 6 != 1 and x % 6 != 5:
            return False
        for i in range(5, int(x ** 0.5) + 1, 6):
            if x % i == 0 or (x + 2) % i == 0:
                return False
        return True

    count = 0
    return
