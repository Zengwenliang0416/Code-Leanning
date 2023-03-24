def que2407(n):
    a = []  # 创建一个空的数组用于存储字母，在该数组中的列名的排列方式时逆序的。
    while n // 26:  # 只要n>26就说明列名至少有两个字母
        b = n % 26
        a.append(chr(64 + b))
        n //= 26
        if n < 26:
            a.append(chr(64 + n))  # Python中ASC码转字符串，因为n=1,2,3,4....，所以将初始值赋值为@的ASC码（64）
    return "".join(a[::-1])


def que2408():
    import datetime
    count = 0
    start = datetime.date(1900, 1, 1)
    end = datetime.date(9999, 12, 31)
    start_id = datetime.date.toordinal(start)
    end_id = datetime.date.toordinal(end)
    while start_id < end_id:
        year = list(str(start.year))
        month = list(str(start.month))
        day = list(str(start.day))
        if sum(map(int,year)) == (sum(map(int,month)) + sum(map(int,day))):
            count += 1
        start = datetime.date.fromordinal(start_id+1)
        start_id = datetime.date.toordinal(start)

    return count
print(que2408())