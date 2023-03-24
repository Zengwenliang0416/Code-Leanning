
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

def que2117():
    
    n = int(input())
    h = list(map(int,input().split()))
    a = [[0 for j in range(6)] for i in range(len(h))]
    def cut(x):
        return int((x//2+1)**0.5//1)

    count = 0
    for i in range(len(h)):
        while h[i]!=1:
            h[i] = cut(h[i])
            count+=1

    return

# print(que2117())
