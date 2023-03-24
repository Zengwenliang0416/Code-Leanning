def que2122():

    n = int(input())
    m = int(input())

    dic = {}
    def sumnum(i):
        return sum(list(map(int,str(i))))
    for i in range(1,n+1):
        dic[i] = sumnum(i)

    ordic = sorted(dic.items(),key=lambda x : x[1])
    print(ordic[m-1][0])
    return 0
que2122()