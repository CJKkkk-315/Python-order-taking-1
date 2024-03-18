from scipy.interpolate import CubicSpline
import pandas as pd
import datetime
import os.path
ext='.xlsx'
files = [f for f in os.listdir() if os.path.isfile(f) and os.path.splitext(f)[1]==ext]
d1 = datetime.date(2010,10,1)
d2 = datetime.date(2013,1,1)
d3 = datetime.date(2017,11,30)
s1 = (d2-d1).days
s2 = (d3-d1).days
for p in files:
    from datetime import datetime
    file = pd.read_excel(p)
    data = pd.DataFrame(file)
    c1 = data.columns[0]
    c2 = data.columns[1]
    c3 = data.columns[2]
    cd = data['测点'].values[0]
    data.drop('测点',axis=1, inplace=True)
    x = []
    y = []
    for i in data.values:
        d = (datetime.strptime(str(i[0]).split(' ')[0], "%Y-%m-%d").date()-d1).days
        if d not in x and d >= 0:
            x.append(d)
            y.append(i[1])
    cs = CubicSpline(x,y,bc_type='not-a-knot')
    x = []
    y = []
    z = []
    import datetime
    for i in range(s1,s2+1):
        x.append(d2 + datetime.timedelta(days = i-s1))
        y.append(round(float(cs(i)),6))
    for i in range(len(x)):
        z.append(cd)
    dic = {c1:z,c2:x,c3:y}
    pd.DataFrame(dic).to_excel('保存数据/' + p,index=None)




