import random
s = input('请输入5个字')
s = list(s)
r = []while True:
    i = random.randint(0,len(s)-1)
    r.append(s[i])
    s.remove(s[i])
    if len(r) == 5:
        break
with open('jieguo.txt','w') as f:
    for i in r:
        f.write(i+' ')