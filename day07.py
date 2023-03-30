def que616():
    count = 0
    for i in range(40):
        for j in range(40):
            for k in range(40):

                if 3**i*5**j*7**k <= 59084709587505:
                    count += 1
                else :
                    break
    print(count - 1)


def nm():
    # 记录选中的数字
    chosen = []  
    # 接收需要处理的数字，目的是为了从n个数里面取出m个数，每个个数都不相同。
    n,m = map(int,input().split())  
    # 排列组合取数函数
    # 函数的参数x代表从哪个数字开始进行排列组合
    def calc(x):
        # 我们需要取的是m个数，如果我们选中的数字已经大于m个了，此时可以直接返回
        if len(chosen) > m:
            return
        # 如果我们需要的数字个数满足不了m个时，直接返回，也就是说这次递归结束
        if len(chosen) + n - x + 1 < m:
            return
        if x == n + 1:
            for i in chosen:
                print(i,end=' ')
            print('')
            return
        calc(x + 1)
        chosen.append(x)
        calc(x + 1)
        chosen.pop()
    calc(1)


order = [0]*20
chosen = [0]*20
n = int(input())
def cala(x):
    if x == n+1:
        ansTem = ''
        for i in range(1, n + 1):
            print(order[i],end=' ')
        print('')