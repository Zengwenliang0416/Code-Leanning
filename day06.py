def que2109():
    n,m,k = map(int,input().split())
    A = []
    for i in range(n):
        A.append(list(map(int,input().split())))
    #创建前缀和矩阵
    sumA = [[0 for i in range(m+1)] for i in range(n+1)]
    #计算行前缀和
    for i in range(1,n+1):
        for j in range(1,m+1):
            sumA[i][j] = sumA[i-1][j] + A[i-1][j-1]
    
    for i in range(n+1):
        for j in range(i,n+1):
            l,r = 1,n+1
    return

def que2385():

    return

def que2186():

    return

def que2114():

    return


def que2108():
    n = int(input())
    ma = int(input())
    A = list(map(int,input().split()))
    mb = int(input())
    B = list(map(int,input().split()))

    r = 0
    p = 1
    m = 1000000007
    for i in range(len(list(A))-1,-1,-1):   #逆序遍历
        k = max(2,max(A[i]+1,B[i]+1))
        r = (r + p * (A[i] - B[i])%m)%m
        p = p*k%m
    print(r)


def que2142():
    s = input()
    a = []
    for i in range(26):
        a.append(s.count(chr(65+i)))
    b = []
    for i in range(26):
        if a[i] == max(a):
            b.append(chr(65+i))
    print("".join(b))

que2142()