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


def que1536():
    # 创建存放三角形的矩阵
    a = [[0]*100]*100
    n = int(input())
    # 为什么第一行要全部为0？
    for i in range(1,n+1):
        a[i] = input().split()
        a[i] = list(map(int,a[i]))
    for i in range(n-1,0,-1):
        for j in range(0,i):
            a[i][j] += max(a[i+1][j],a[i+1][j+1])
    print(a[1][0])
    

def que505():
    N=int(input())
    nums=[list(map(int,input().split()))for i in range(N)]
    # 从第二行开始，每一行加上上一行左右节点的最大值
    # 这里存在两个边界条件，当节点为第一个节点和最后一个节点时
    for i in range(1,N):
        for j in range(0,i+1):#从0~i
            if j==0:
                nums[i][j]+=nums[i-1][j]
            elif j==i:
                nums[i][j]+=nums[i-1][j-1]
            else:
                nums[i][j]+=max(nums[i-1][j-1:j+1])
    # 判断N是奇数还是偶数，由于左右两边要走的步数差值不能大于1
    # 所以对于奇数而言一定是最后一排最中间的数字，对偶数而言一定是中间两个数字的最大值
    if N&1:
        print(nums[-1][N//2])
    else:
        print(max(nums[-1][N//2-1],nums[-1][N//2]))

def que000():
    a = input().split()
    b = []
    for i in a:
        if i == 'J':
            b.append(11) 
        elif i == 'Q':
            b.append(12)
        elif i == 'K':
            b.append(13)
        elif i == 'A':
            b.append(1)
        else:
            b.append(int(i))

    c = [[] for i in range(10)]
    c[0].append(b[0])
    for i in range(1,6):
        for j in range(len(c[i-1])):
            c[i].append(c[i-1][j]+b[i])
            c[i].append(c[i-1][j]-b[i])
            c[i].append(c[i-1][j]*b[i])
            c[i].append(c[i-1][j]//b[i])
    flag = 0
    if 42 in c[5]:
        flag =1
    if (flag == 1):
        print('YES')
    else:
        print('NO')


def que760():
    def f(n):
        global res
        if n == 1:
            return
        for i in range(1, n//2+1):
            res += 1
            f(i)
    n = int(input())
    res = 1
    f(n)
    print(res)

# n,k = map(int,input().split())
# dp = [[0 for j in range(210)] for i in range(210)]
# for i in range(1,n+1):
#     dp[i][1] = 1
#     dp[i][i] = 1

# for i in range(3,n+1):
#     for j in range(2,k+1):
#         if i > j:
#             dp[i][j] = dp[i-j][j] + dp[i-1][j-1]
# print(dp[n][k])


b = [0] * 105
c = [0] * 105
n = int(input())
i = 0
while c[i] < n:
   i += 1
   b[i] = i + b[i - 1]
   c[i] = c[i - 1] + b[i - 1] + 1
print(i)