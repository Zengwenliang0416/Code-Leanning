def que2381():
    def re(a):
        if list(str(a))[::-1] == list(str(a)):
            return True
        return False

    for i in range(1, 10000):
        a = i * (i + 1) // 2
        if re(a) and a > 20220514:
            print(a)
            break


def que2385():
    n = int(input().split())
    a = list(map, int(input().split()))

    def isPrime(n):
        if n == 2 or n == 3:
            return True
        elif n % 6 != 1 and n % 6 != 5:
            return False
        else:
            for i in range(5, int(n ** 0.5) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True