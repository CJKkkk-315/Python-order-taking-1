import  pandas  as pd
import matplotlib.pyplot as plt
df=pd.read_csv('葡萄酒品质数据集.csv')
print(df.isnull().sum())
print(df.describe())