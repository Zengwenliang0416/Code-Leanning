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
    s = list(input())
    
    count = 0
    l ,r = 0,0
    for i in range(1,len(s)-1):
            while len(s) > 2:
                if s[i] == s[i-1] and s[i]!=s[i+1]:
                    l == i
                if s[i] != s[i-1] and s[i]==s[i+1]:
                    r == i+1
                    del s[l,r+1]
                if count >= 2**64:
                    print("".join(s))
                    break
            print("".join(s))
        

que2127()