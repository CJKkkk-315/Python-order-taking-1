import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
#引入必要的包
confirmed_df = pd.read_csv('time_series_covid19_confirmed_global.csv')
deaths_df = pd.read_csv('time_series_covid19_deaths_global.csv')
recoveries_df = pd.read_csv('time_series_covid19_recovered_global.csv')
#分别利用pandas读取确诊，治愈与死亡文件
#获得所有列名
cols = confirmed_df.keys()
confirmed = confirmed_df.loc[:, cols[4]:cols[-1]]
deaths = deaths_df.loc[:, cols[4]:cols[-1]]
recoveries = recoveries_df.loc[:, cols[4]:cols[-1]]
dates = confirmed.keys()
world_cases = []
total_deaths = []
mortality_rate = []
recovery_rate = []
total_recovered = []
print(deaths.head(10))
for i in dates:
    confirmed_sum = confirmed[i].sum()
    death_sum = deaths[i].sum()
    recovered_sum = recoveries[i].sum()

    # 计算确证，死亡的数量
    world_cases.append(confirmed_sum)
    total_deaths.append(death_sum)

    # 计算康复率和死亡率
    mortality_rate.append(death_sum / confirmed_sum)
    recovery_rate.append(recovered_sum/confirmed_sum)
    #获得每日增长值和增长的平均值
def daily_increase(data):
    d = []
    for i in range(len(data)):
        if i == 0:
            d.append(data[0])
        else:
            d.append(data[i]-data[i-1])
    return d

def moving_average(data, window_size):
    moving_average = []
    for i in range(len(data)):
        if i + window_size < len(data):
            moving_average.append(np.mean(data[i:i+window_size]))
        else:
            moving_average.append(np.mean(data[i:len(data)]))
    return moving_average

# 平均值窗口大小
window = 7

# 以确证病例
world_daily_increase = daily_increase(world_cases)
world_confirmed_avg= moving_average(world_cases, window)
world_daily_increase_avg = moving_average(world_daily_increase, window)

# 死亡病例
world_daily_death = daily_increase(total_deaths)
world_death_avg = moving_average(total_deaths, window)
world_daily_death_avg = moving_average(world_daily_death, window)


#治愈病例
world_daily_recovery = daily_increase(total_recovered)
world_recovery_avg = moving_average(total_recovered, window)
world_daily_recovery_avg = moving_average(world_daily_recovery, window)
days_in_future = 10
future_forcast = np.array([i for i in range(len(dates)+days_in_future)]).reshape(-1, 1)
adjusted_dates = future_forcast[:-10]
#将整数转换为日期格式，方便后续的可视化
start = '1/22/2020'
start_date = datetime.datetime.strptime(start, '%m/%d/%Y')
future_forcast_dates = []
for i in range(len(future_forcast)):
    future_forcast_dates.append((start_date + datetime.timedelta(days=i)).strftime('%m/%d/%Y'))


#数据处理完毕 绘制确诊，死亡病例以及死亡率


#数据平滑处理
def flatten(arr):
    a = []
    arr = arr.tolist()
    for i in arr:
        a.append(i[0])
    return a
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
adjusted_dates = adjusted_dates.reshape(1, -1)[0]
plt.figure(figsize=(16, 10))
plt.plot(adjusted_dates, world_cases)
plt.plot(adjusted_dates, world_confirmed_avg, linestyle='dashed', color='orange')
plt.title('#确诊病例随时间变化', size=30)
plt.xlabel('自2020年1月22日起', size=30)
plt.ylabel('数量', size=30)
plt.legend(['全球确诊人数', '平均 {} 天'.format(window)], prop={'size': 20})
plt.xticks(size=20)
plt.yticks(size=20)
plt.show()

plt.figure(figsize=(16, 10))
plt.plot(adjusted_dates, total_deaths)
plt.plot(adjusted_dates, world_death_avg, linestyle='dashed', color='orange')
plt.title('死亡人数随时间变化', size=30)
plt.xlabel('自2020年1月22日起', size=30)
plt.ylabel('数量', size=30)
plt.legend(['全球死亡人数', '平均 {} 天'.format(window)], prop={'size': 20})
plt.xticks(size=20)
plt.yticks(size=20)
plt.show()

#以国家为个体，计算各个国家的新冠疫情数据
def country_plot(x, y1, y2, y3, country):
    confirmed_avg = moving_average(y1, window)
    confirmed_increase_avg = moving_average(y2, window)
    death_increase_avg = moving_average(y3, window)

    plt.figure(figsize=(16, 10))
    plt.plot(x, y1)
    plt.plot(x, confirmed_avg, color='red', linestyle='dashed')
    plt.legend(['{} 确诊病例'.format(country), '平均 {} 天'.format(window)], prop={'size': 20})
    plt.title('{} 确诊病例'.format(country), size=30)
    plt.xlabel('自从1/22/2020以来', size=30)
    plt.ylabel('数量', size=30)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.bar(x, y2)
    plt.plot(x, confirmed_increase_avg, color='red', linestyle='dashed')
    plt.legend(['平均{}天'.format(window), '{} 每日增长确诊病例'.format(country)],
               prop={'size': 20})
    plt.title('{} 每日增长确诊病例'.format(country), size=30)
    plt.xlabel('自从1/22/2020以来', size=30)
    plt.ylabel('数量', size=30)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

    plt.figure(figsize=(16, 10))
    plt.bar(x, y3)
    plt.plot(x, death_increase_avg, color='red', linestyle='dashed')
    plt.legend(['平均{}天'.format(window), '{} 每日增长死亡病例'.format(country)],
               prop={'size': 20})
    plt.title('{} 每日增长死亡病例'.format(country), size=30)
    plt.xlabel('自从1/22/2020以来', size=30)
    plt.ylabel('数量', size=30)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()

#编写函数获得国家索引
def get_country_info(country_name):
    country_cases = []
    country_deaths = []
    country_recoveries = []

    for i in dates:
        country_cases.append(confirmed_df[confirmed_df['Country/Region'] == country_name][i].sum())
        country_deaths.append(deaths_df[deaths_df['Country/Region'] == country_name][i].sum())
        country_recoveries.append(recoveries_df[recoveries_df['Country/Region']==country_name][i].sum())
    return (country_cases, country_deaths)

#不同国家的新冠疫情可视化
def country_visualizations(country_name):
    country_info = get_country_info(country_name)
    country_cases = country_info[0]
    country_deaths = country_info[1]

    country_daily_increase = daily_increase(country_cases)
    country_daily_death = daily_increase(country_deaths)

    country_plot(adjusted_dates, country_cases, country_daily_increase, country_daily_death, country_name)

countries = ['India', 'US', 'Russia', 'United Kingdom', 'France']

#将一些主要国家放在同一张图中进行对比
for country in countries:
    country_visualizations(country)
compare_countries = ['India', 'US', 'Brazil', 'Russia', 'United Kingdom', 'France']
graph_name = ['确诊人数对比', '死亡人数对比']

for num in range(2):
    plt.figure(figsize=(16, 10))
    for country in compare_countries:
        plt.plot(get_country_info(country)[num])
    plt.legend(compare_countries, prop={'size': 20})
    plt.xlabel('自从1/22/2020以来', size=30)
    plt.ylabel('数量', size=30)
    plt.title(graph_name[num], size=30)
    plt.xticks(size=20)
    plt.yticks(size=20)
    plt.show()
