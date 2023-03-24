
def que2122():

    n = int(input())
    m = int(input())

    dic = {}
    """
    说明:计算输入数字的数位和
    ------------------------------------
    变量:i
    ------------------------------------
    返回:数位之和，eg. i = 10 return 1 + 0 = 1
    ------------------------------------
    """
    def sumnum(i):
        return sum(list(map(int,str(i))))
    for i in range(1,n+1):
        dic[i] = sumnum(i)
    
    ordic = sorted(dic.items(),key=lambda x : x[1])
    print(ordic[m-1][0])
    return 0
que2122()
