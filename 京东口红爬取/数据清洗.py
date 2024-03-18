import difflib
import csv
def com(s1,s2):
    return difflib.SequenceMatcher(None,s1,s2).quick_ratio()
data = []
res = []
with open('URL.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        data.append(row)
for i in range(len(data)):
    flag = 1
    for j in range(i+1,len(data)):
        if com(data[i][1],data[j][1]) > 0.6:
            flag = 0
            break
    if flag:
        res.append(data[i])
with open('URL（去重）.csv', 'w', newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)