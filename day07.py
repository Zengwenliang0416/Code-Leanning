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


def nm(n,m):
    # 记录选中的数字
    chosen = []  
    # 接收需要处理的数字，目的是为了从n个数里面取出m个数，每个个数都不相同。
    # n,m = map(int,input().split())  
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


# n = 3
# nm(4,2)
# for i in range(1, n+1):
#     nm(n,i)




# order = [0]*20
# chosen = [0]*20
# n = int(input())
# def cala(x):
#     if x == n+1:
#         ansTem = ''
#         for i in range(1, n + 1):
#             print(order[i],end=' ')
#         print('')
#         return
#     for i in range(1,n+1):
#         if(chosen[i] == 1):
#             continue
#         order[x] = i
#         chosen[x] = 1
#         cala(x+1)
#         chosen[i] = 0
#         order[x] = 0
# cala(1)

def que269():
    from itertools import permutations
    # 用来保存初始输入以结束循环
    olds = input()
    # 将输入的字符串变为列表后进行排序
    news = list(olds)
    news.sort()
    # 记录当前串的序号，因为前面的代码已经对输入的字符进行了排序了，所以这个地方的cut = 0
    cut = 0
    # 开始从'abcd'的第一个子串进行逐个遍历，直到出现能够终止循环的子串为止
    # 每一个element为一个元组
    for element in permutations(news):
        print(element)
        a = ''.join(element)
        if olds == a:
            print(cut)
            break
        cut += 1

def que572():
    from itertools import permutations
    # 用来保存初始输入以结束循环
    n = int(input())
    m = int(input())
    olds = list(map(str,input().split()))
    # 将输入的字符串变为列表后进行排序
    olds.sort()
    news = olds[::-1]
    # 记录当前串的序号，因为前面的代码已经对输入的字符进行了排序了，所以这个地方的cut = 0
    cut = 1
    # 开始从'abcd'的第一个子串进行逐个遍历，直到出现能够终止循环的子串为止
    # 每一个element为一个元组
    for element in permutations(olds):
        # a = ''.join(element)
        if olds == list(element):
            record = cut
        if cut == record + m:
            a = list(map(int,element))
            for i in range(len(a)):
                print(a[i],end=' ')
            print('')
        cut += 1

def isPrime(x):
    if x == 2 or x == 3:
        return True
    if x%6 !=1 and x%6 != 5:
        return False
    for i in range(5,int(x**0.5)+1,6):
        if x%i == 0 or x%(i+2) == 0:
            return False
    return True

# n = int(input())
# m = int(input())
# nums = list(map(int,input().split()))
# def find_next(nums):
#     for i in range(n-1,0,-1):
#         if nums[i] > nums[i-1]:
#             for j in range(n-1,i-1,-1):
#                 if nums[j] > nums[i-1]:
#                     nums[j], nums[i-1] = nums[i-1], nums[j]
#                     return nums[:i] + nums[:i-1:-1]
# for i in range(m):
#     nums = find_next(nums)
# print("".join([str(i) for i in nums]))

def queunkown():
    n,S = map(int,input().split())
    a = list(map(int,input().split()))
    suma = 0
    ans = 1e8
    i,j = 0,0
    while i < len(a):
        if suma < S:
            suma += a[i]
            i += 1
        else:
            ans = min(i-j,ans)
            suma -= a[j]
            j += 1
    if ans == 1e8:
        print('0')
    else:
        print(ans)

def que1374():
    n,C = map(int,input().split())
    a = list(map(int,input().split()))
    # 由于对于乱序数组进行差值计算时间复杂度过大，因此先对数组进行排序，降低时间复杂度
    a.sort()
    # 设置左右指针，左指针用来记录差值小于0的下标
    l,r = 0,0
    count = 0
    for i in range(n):
        while l<n and a[l]- a[i] < C:
            l += 1
        while r<n and a[r] - a[i] <= C:
            r += 1
        r -= 1
        if r > 0 and a[r]-a[i]== C and a[l] - a[i] == C:
            count += r - l + 1
    print(count)
        
n,m,k = map(int,input().split())
a = list(map(int,input().split()))

def check(b):
    b.sort()
    if b[-k] >= m:
        return True
    else:
        return False
count = 0
l,r = 0,k
while r <= n:
    if check(a[l:r]):
        # print(a[l:r])
        count = count + n-r+1
        l += 1
        r = l + k
    else:
        r += 1

print(count)