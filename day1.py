def que1444():
    for i in range(1, 2022):
        if (i * 1000000007 + 999999999) % 2021 == 0:
            return int((i * 1000000007 + 999999999) / 2021)


def que1446():
    return ord('L')


def que1554(a, b):
    from sys import setrecursionlimit
    setrecursionlimit(int(1e5))
    import math
    from functools import lru_cache
    @lru_cache()
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    return math.gcd(fib(a), fib(b))


def que217(n, m, p):
    from sys import setrecursionlimit
    setrecursionlimit(int(1e5))
    from functools import lru_cache
    @lru_cache()
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    sum = 0
    for i in range(1, n + 1):
        sum += fib(i)

    return ((sum) % fib(m)) % p


def que2107(n):
    a = []
    for i in range(1, n + 1):
        a.append(2 * max(i - 1, n - i))
    return a


def que174(n, s, a):
    avg = s / n
    sum1 = 0
    a.sort()
    for i in range(n):
        if a[i] * (n - i) < s:
            sum1 += pow(a[i] - avg, 2)
            s = s - a[i]
        else:
            new_avg = s / (n - i)
            sum1 += pow(new_avg - avg, 2) * (n - i)
            break
    return "{:.4f}".format((sum1 / n) ** 0.5)

def que2417(s):
    s0 = 'lanqiao'
    if s.lower() != s0 :
        return "no"
    else:
        return "yes"

def que2080():
    n = int(input())
    a = list(map(int,input().split()))
    suma = sum(a)
    s = 0
    for i in range(len(a)):
        suma-=a[i]
        s+=a[i]*suma
    
    return s

def que2118(s='WHERETHEREISAWILLTHEREISAWAY'):
    a = list(s)
    a.sort()
    return "".join(a)

def que2098():
    a,b,n = map(int,input().split())
    sumque = 5 * a + 2 * b
    c = n % sumque
    print(c)
    if c:
        d = n // sumque
        que = n - d * sumque 
        for i in range(1,8):                
            if i >= 6:
                que -= b
            else:
                que -=a
            if que<=0:
                return d*7+i
    else:
        return int((n//sumque)*7)

def que2096():
    from datetime import date
    start = date(2022,1,1)
    end = date(2022,12,31)
    start_id = date.toordinal(start)
    end_id = date.toordinal(end)
    count = 0
    while start_id <= end_id:        
        s = str(start)
        s = s.replace("-","")
        if '012' in s or '123' in s or '234' in s or '345' in s or '456' in s or '678' in s or '789' in s:
            count+=1
        start = date.fromordinal(start_id+1)
        start_id = date.toordinal(start)

    return count

def que2120():
    a = list(input())
    l = 1189
    h = 841
    for i in range(int(a[-1])):
        tem = max(l,h)//2
        h = min(l,h)
        l = tem

        
    print(max(l,h))
    print(min(l,h))

def que2097():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0]*n
    for i in range(1,n):
        b[i] = b[i-1] + a[i-1]
    
    def check(y):
        for i in range(1,n-y+1):
            r = i + y -1
            if b[r] - b[i-1] < 2 * x:
                return False
        return True

    l,r = 1,n
    res = -1
    while l<=r:
        mid = (l+n) // 2
        if check(mid):
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

def que2122():

    n = int(input())
    m = int(input())

    dic = {}
    def sumnum(i):
        return sum(list(map(int,str(i))))
    for i in range(1,n+1):
        dic[i] = sumnum(i)
    print(dic)

    return 0
que2122()