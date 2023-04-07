def que2122():
    n = int(input())
    m = int(input())

    dic = {}
    # 计算数位和
    def sumnum(i):
        return sum(list(map(int, str(i))))

    for i in range(1, n + 1):
        dic[i] = sumnum(i)
    a = dic.items()
    # 将字典按照值进行排序
    ordic = sorted(dic.items(), key=lambda x: x[1])
    print(ordic[m - 1][0])
    return 0
que2122()
from math import *

def que2117():
    # #  55%
    # n = int(input())
    # h = list(map(int, input().split()))
    # a = [[0 for j in range(1)] for i in range(len(h))]

    # def cut(x):
    #     return int((x // 2 + 1) ** 0.5 // 1)

    # count = 0
    # for i in range(len(h)):
    #     while h[i] != 1:
    #         h[i] = cut(h[i])
    #         a[i].append(h[i])
    #         count += 1
    # for i in range(n - 1):
    #     for j in range(min(len(a[i]), len(a[i + 1]))):
    #         if a[i][j] == 0:
    #             continue
    #         elif a[i][j] == a[i + 1][j]:
    #             if a[i][j] == 1 and a[i][j - 1] != 0:
    #                 continue
    #             count -= 1
    # print(count)
    def msqrt(x):
        l = 0
        r = x
        while l <= r:
            mid = l+r >> 1 
            if mid*mid <= x: 
                s = mid; 
                l = mid + 1; 
            else :
                r = mid - 1; 
        return s
    n=int(input())
    l=list(map(int,input().split()))

    all_lis = []
    ans = 0

    for i in range(n):
        li = [1]  # 确保剪裁后的矩阵中有值
        while l[i]>1:
            ans+=1
            li.append(l[i])
            # l[i] = floor(sqrt(floor(l[i]/2)+1))
            l[i] = msqrt(floor(l[i]/2)+1)
        all_lis.append(li)
    
    for i in range(1,n):
        # 消除初始长度1的影响，因为在all_lis的数组中会记录
        # 除最后一次施法的长度（即为1）。
        ans+=1  
        # 只要在相邻的两颗竹子施法后的长度相等的话就说明可以一起使用魔法，魔法
        # 次数-1
        for j in all_lis[i-1]:
            if j in all_lis[i]:
                ans-=1
    print(ans)

que2117()


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




def que2097():
    n,x = map(int,input().split())
    H = list(map(int,input().split()))
    sum_H = [0]*n
    #首先处理一下，像这种需要计算连续数组值时使用前缀和是能够节省时间复杂度的，计算代码相对来说也比较简单
    #思路：创建一个比原数组多一个长度的全0数组，随后循环相加，这里要注意的是，循环从1开始，边界值在n
    #关于边界值为n的解释，我们创建了一个数组为n-1的列表H，实际上这个列表中的最后一项为n-2，同理，sum_H的最后一项
    #为n-1，所以为了防止越界，我们的边界值分别为1，n
    for i in range(1,n):
        sum_H[i] = sum_H[i-1] + H[i-1]
    #检查部分为核心代码，这里要思考的是，我的跳跃能力满足什么条件时才能往返2*x次呢？
    #每次跳到一个石头上石头上的数字-1，我肯定是想跳到我能跳到的最远的或者最高的，用来保证我能跳回来
    #但是算法过于复杂，换个思路，当在我跳跃范围之内，所有石头的高度之和能够大于或者等于我跳2*x次不是一样吗
    #两个思路的差异在于，第一个思路太偏向于单个石头，而第二个思路从跳跃范围之和考虑，使用前缀和就能完美解决
    def check(y):
        #搞清楚边界是关键，用除法去找整段太麻烦，你要想一想，如果你要知道你总共有几段跳跃距离，你只要知道你
        #最后一步落在哪里就行了，显然是落在n-y-1这个石头上
        for i in range(n-y):
            #左右边界其实很好确定
            #左边界当然是第i块石头，因为我每次检查的就是我的跳跃范围内的石头之和是否大于2*x，所以我的
            #右边界当然是i+y，只要在这个范围内的石头高度之和大于2*x，那在y跳跃能力之下是一定可以上x次课的
            if sum_H[i+y]-sum_H[i]<2*x:
                return False
        return True
    #使用二分法将符合条件的最小跳跃值计算出来
    l,r = 1,n
    res = -1
    while l<=r:
        mid = (l+r) // 2
        if check(mid):
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    print(res)
# que2097()

