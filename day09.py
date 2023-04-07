def que1508():
    # N皇后问题
    x = [0]*15
    n = 0
    sum = 0
    # 传进来的参数为第k个皇后
    # 需要判断的是现在的k个皇后是否满足以下三个条件：
    # 不在同一行
    # 不在同一列
    # 不在对角线
    def pd(k):
        for i in range(1,k):
            # 结合斜率判断是否在对角线上
            if abs(k - i) == abs(x[k] - x[i]):
                return 0
            # 判断第k个皇后和前面所有的皇后是否在同一列
            elif x[k] == x[i]:
                return 0
        return 1

    def check(a):
        if a > n:
            # 当a>n也就说明所有皇后已经放置完成
            # 这里要指出的是，这个只是所有皇后放置完成的一种情况，因此sum+=1
            global sum
            sum += 1
        else:
            return False
        return True

    def DFS(a):
        # 这里要判断的情况是所有所有皇后是否放置完毕
        if check(a):
            # 当a大于n时，开始回溯，找其他放置皇后的方法
            return
        else:
            for i in range(1,n+1):
                # 由于我们使用a代表第几个皇后，因此不再需要再去考虑行数的问题
                # 此时我们针对每一列做搜索
                # x[a] = i表示的是第a个皇后在第i列
                x[a] = i
                # 判断同行同列以及对角线上是否有皇后
                if pd(a):
                    # 如果第a个皇后能够放在棋盘上，则继续对下一个皇后使用DFS
                    DFS(a+1)
                else:
                    # 当第a个皇后不能放在第i列时，结束循环进入下一列
                    continue
    n = int(input())
    # 先找到第一个皇后的位置
    DFS(1)
    print(sum)


# n = int(input())
# x_label = list(map(int,input().split()))
# y_label = list(map(int,input().split()))

# dx = [0,0,-1,1]
# dy = [1,-1,0,0]
# res = []
# pos = [[]*n]
# start = 0
# for i in range(n):
#     pos.append([])
#     for j in range(n):
#         pos[i].append(start)
#         start += 1
# pos.pop()

# def pd(nowx,nowy):
    
#     return

# def check(nowx,nowy):
#     if nowx == n and nowy == n:
#         return True
#     else:
#         return False


# def DFS(nowx,nowy):
#     if check(nowx,nowy):
#         return
#     else:
#         for i in range(4):
#             nextx += dx
#             nexty += dy
#             if pd(nextx,nexty):
#                 DFS(nextx,nexty)
#             else:
#                 continue

from collections import *
def quemikong():
    mp = []
    for i in range(30):
        mp.append(list(map(int,input())))
    k = ('D','L','R','U')
    dir = [(1,0),(0,-1),(0,1),(-1,0)]
    vis = [[0]*50 for i in range(30)]
    fater = [['']*50 for i in range(30)]

    def dfs(x,y):
        if x == 0 and y == 0:
            return
        if fater[x][y] == 'D': dfs(x-1,y)
        if fater[x][y] == 'L': dfs(x,y+1)
        if fater[x][y] == 'R': dfs(x,y-1)
        if fater[x][y] == 'U': dfs(x+1,y)
        print(fater[x][y],end="")

    def check(x,y):
        if x==29 and y==40:
            return True
    def pd(x,y):
        if x<0:
            return False
        elif x >= 30:
            return False
        elif y < 0:
            return False
        elif y >= 50 :
            return False
        elif vis[x][y] == 1:
            return False
        elif mp[x][y] == 1:
            return False
        else:
            return True

    def bfs(x,y):
        global fater
        global vis
        q = deque()
        q.append((x,y))
        vis[x][y] = 1
        while q:
            now = q.popleft()
            if check(now[0],now[1]):
                return
            else:
                for i in range(4):
                    next = [0,0]
                    next[0] = now[0] + dir[i][0]
                    next[1] = now[1] + dir[i][1]
                    if not pd(next[0],next[1]):
                        continue
                    else:
                        vis[next[0]][next[1]] = 1
                        q.append((next[0],next[1]))
                        fater[next[0]][next[1]] = k[i]
    bfs(0,0)
    dfs(29,49)
    print('')



def que642():
    # 跳蚂蚱
    def insertQueue(q,dir,news,vis):
        pos = news[1]
        status = news[0]
        insertPos = (pos + dir + 9)%9
        t = list(status)
        t[pos],t[insertPos] = t[insertPos],t[pos]
        addStatus = "".join(t)
        if addStatus not in vis:
            vis.add(addStatus)
            q.append((addStatus,insertPos,news[2]+1))

    jump = [-1,-2,1,2]
    q = deque()
    q.append(("012345678",0,0))
    vis = set()
    vis.add("012345678")

    def check(s):
        if s == '087654321':
            return True
        return False

    while q:
        news = q.popleft()
        if check(news[0]):
            print(news[2])
            break
        for i in range(4):
            insertQueue(q,jump[i],news,vis)
