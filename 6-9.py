
# 4
a = input('').split(' ')
username = a[0]
password = a[1]
yue = float(a[2])
quqian = float(a[3])
if username != '12345' or password != '567890':
    print('帐号或密码错误')
else:
    if yue < quqian:
        print('余额不足')
    else:
        if quqian < 20000:
            print('取款成功:{:.2f}-{:.2f}={:.2f}'.format(yue,quqian,yue-quqian))
        else:
            print('超过单次取款限额')

