def que2060():
    print(4+19+21*20)


def que2131():
    for i in range(10**17):
        if i % 2 == 1 and i % 4 == 1 and i % 8 == 1 and i % 41 == 1:
            if i % 3 == 2 and i % 9 == 2 and i % 3 == 2:
                
                print()



def que2155():
    # # 80%
    # n = int(input())
    # ans = 0
    # #从2开始进行质因子分解
    # i = 2
    # while i * i <= n:
    #     if n % i == 0:
    #         ans += 1
    #         while n % i == 0:
    #             n //= i
    #     i += 1
    # if n != 1:
    #     ans += 1
    # print(ans)

    # 100%
    n=int(input())
    res=dict()

    for i in [2,3]:
        if n%i==0:
            res[i]=1
            while n!=i and n%i==0:
                n//=i
    #6n法筛选素数
    for i in range(6,int(n**0.5)+1,6):
        for j in [i-1,i+1]:
            if n%j==0:
                res[j]=1
                while n!=j and n%j==0:
                    n//=j
    # if n >0 and n not in res:
    #   res.append(n)
    if n>0:
    # res.add(i)
        res[n]=1
    print(len(res))

def que2127():
    # 58%
    s = list(input())
    last_lenth = 0
    while True:
        lenth  = len(s)
        if lenth == 0:
            print("EMPTY")
            break
        if last_lenth == lenth:
            print("".join(s))
            break
        new_s = [0]*lenth
        for i in range(lenth):
            if i-1 >= 0 and i+1<lenth and s[i-1] == s[i] and s[i]!=s[i+1]:
                new_s[i] = new_s[i+1] = 1
            if i-1>=0 and i+1<lenth and s[i-1] != s[i] and s[i]==s[i+1]:
                new_s[i] = new_s[i-1] = 1
        tem_s = []
        for i in range(lenth):
            if new_s[i] == 0:
                tem_s.append(s[i])
        s = tem_s
        last_lenth = lenth
que2127()


        

