def que600():
    a = [1,1,1]
    for i in range(3,20190325):
        a.append((a[i-1]+a[i-2]+a[i-3])%10000)

    print(a[20190323])

def que191():
    n = int(input())
    b = []
    res = 0
    crub = ['2','0','1','9']
    for j in range(n+1):
        for i in crub:
            if i in list(str(j)):
                b.append(j)
    print(sum(list(set(b))))


def que605():
    print()


def que606():
    a = 0
    n = 2019
    for i in range(1,672):
        for j in range(i+1,1009):
            k = 2019 - i - j
            if (k>j and '2' not in str(i)+str(j)+str(k) 
                and '4' not in str(i)+str(j)+str(k)):
                a+=1
    print(a)
que606()    


