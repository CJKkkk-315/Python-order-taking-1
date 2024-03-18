from random import randint
a = [0,0,0,0,1]
for i in range(5):
    b = randint(0,4-i)
    if a[b] == 1:
        print('中了')
    else:
        print('没中')
    del a[b]