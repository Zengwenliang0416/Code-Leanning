def que1444():
    # 相乘
    # 通过算数变换的关系将搜索范围变小可以加快速度
    for i in range(1, 2022):
        if (i * 1000000007 + 999999999) % 2021 == 0:
            return int((i * 1000000007 + 999999999) / 2021)


def que1446():
    # ASC与字符之间的转换
    print(ord('L'))
    # 如果要将数字转换为字符的话采用以下方式
    # print(chr(ord('L')))

def memorized_storage_fib(n):
    # 记忆化存储矩阵的大小不能太大，否则容易出现错误，无法正常计算
    # 创建记忆化存储矩阵，不需要对函数进行反复调用
    a = [0 for i in range(100)]
    # 主体斐波那契函数
    def fib1(n):
        # 如果之前的值已经计算出来，那么我们可以直接取用，不用对
        # 函数进行调用
        if a[n]!=0:
            return a[n]
        # 当n为1或者2时，将值存入记忆化存储矩阵
        if n == 1 or n == 2:
            a[n] = 1
            return a[n]
        # 使用递归计算斐波那契数列中每个数组的值
        a[n] = fib1(n-1) + fib1(n-2)
        return a[n]
    print(fib1(n))

def que1554(a, b):
    import math
    # 如果要加快递归的速度，可以采用如下的代码，也是创建存储空间
    # 键入方式：1.sys.slim;     2.slim(1e5);    3.fr fu im lr;  4.@lr()
    from sys import setrecursionlimit 
    setrecursionlimit(int(1e5))
    from functools import lru_cache
    # 必须在函数的头部位置
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
    print(((sum) % fib(m)) % p)


def que2107(n):
    # 修剪灌木
    a = []
    for i in range(1, n + 1):
        a.append(2 * max(i - 1, n - i))
    for i in range(len(a)):
        print(a[i])


def que174():
    n,s = map(int,input().split())
    a = list(map(int,input().split()))
    # 计算初始均值
    avg = s / n
    # 计算初始金额
    sum1 = 0
    # 进行排序处理
    a.sort()
    # i代表第几个人
    for i in range(n):
        # 当第i个人的钱数乘以剩下的人数不够更新后的总数时，说明这个人要出所有的钱
        if a[i] * (n - i) < s:
            sum1 += pow(a[i] - avg, 2)
            s = s - a[i]
        # 当大于总数时，第i个人需要和后面的虽有人平摊还剩下的金额（更新均值）
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

