def que2119():
    day_per_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    def check_D(D):
        month = D // 100
        day = D % 100
        if month < 1 or month > 12:
            return 0
        if day < 1 or day > day_per_month[month]:
            return 0 
        return 1
    def check_H(H):
        h = H // 100
        m = H % 100
        if h < 0 or h > 23:
            return 0 
        if m < 0 or m > 59:
            return 0 
        return 1
    ans = 0
    for a in range(10):
        for b in range(10):
            if a == b:
                continue
            N_Y,N_D,N_H = 4,0,0
            A = [a,a,a,a]
            for i in range(4):
                A[i] = b
                B = "".join(list(map(str,A)))
                number = int(B)
                # number = 0
                # for j in A:
                    # number = number * 10 +j
                N_D = check_D(number) + N_D
                N_H = check_H(number) + N_H
                A[i] = a
            ans += N_Y*N_H*N_D
    print(ans)



def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def memorized_storage_fib(n):
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


    


