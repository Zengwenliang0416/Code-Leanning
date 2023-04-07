def que110():
    Maxn = 2000000
    fa = []
    def init():
        for i in range(Maxn + 1):
            fa.append(i)
    def find(x):
        if fa[x] == x:
            return x
        else:
            fa[x] = find(fa[x])
            return fa[x]
    def merge(x,y):
        fa[find(x)] = find(y)
    n,m,k = input().split()
    Maxn = m*n+100
    init()
    for _ in range(k):
        a,b = int(input().split())
        merge(a,b)
    ans = 0
    for i in range(1,m*n):
        if fa[i] == i:
            ans += 1
    print(ans)

def que364():
    # 跳石头
    len, n, m = map(int,input().split())
    stone = []
    for i in range(n):
        stone.append(int(input()))
    stone.append(len)

    def check(d):
        num = 0
        pos = 0
        for i in range(0,n+1):
            if (stone[i]-pos <d):
                num += 1
            else:
                pos = stone[i]
            if num <= m:
                return True
            else:
                return False
    l,r = 0,len
    while l < r:
        mid = (l+r+1)//2
        if check(mid):
            l = mid
        else:
            r = mid - 1
    print(l)


