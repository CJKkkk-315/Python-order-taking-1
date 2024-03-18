with open('cookie.txt','r') as f:
    data = f.read()
print(data)
for i in data.split('#####'):
    print(i)