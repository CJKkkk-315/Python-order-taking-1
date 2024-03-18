# encoding: utf-8

g_lunar_month_day = [
    0x00752, 0x00ea5, 0x0ab2a, 0x0064b, 0x00a9b, 0x09aa6, 0x0056a, 0x00b59, 0x04baa, 0x00752,  # 1901 ~ 1910
    0x0cda5, 0x00b25, 0x00a4b, 0x0ba4b, 0x002ad, 0x0056b, 0x045b5, 0x00da9, 0x0fe92, 0x00e92,  # 1911 ~ 1920
    0x00d25, 0x0ad2d, 0x00a56, 0x002b6, 0x09ad5, 0x006d4, 0x00ea9, 0x04f4a, 0x00e92, 0x0c6a6,  # 1921 ~ 1930
    0x0052b, 0x00a57, 0x0b956, 0x00b5a, 0x006d4, 0x07761, 0x00749, 0x0fb13, 0x00a93, 0x0052b,  # 1931 ~ 1940
    0x0d51b, 0x00aad, 0x0056a, 0x09da5, 0x00ba4, 0x00b49, 0x04d4b, 0x00a95, 0x0eaad, 0x00536,  # 1941 ~ 1950
    0x00aad, 0x0baca, 0x005b2, 0x00da5, 0x07ea2, 0x00d4a, 0x10595, 0x00a97, 0x00556, 0x0c575,  # 1951 ~ 1960
    0x00ad5, 0x006d2, 0x08755, 0x00ea5, 0x0064a, 0x0664f, 0x00a9b, 0x0eada, 0x0056a, 0x00b69,  # 1961 ~ 1970
    0x0abb2, 0x00b52, 0x00b25, 0x08b2b, 0x00a4b, 0x10aab, 0x002ad, 0x0056d, 0x0d5a9, 0x00da9,  # 1971 ~ 1980
    0x00d92, 0x08e95, 0x00d25, 0x14e4d, 0x00a56, 0x002b6, 0x0c2f5, 0x006d5, 0x00ea9, 0x0af52,  # 1981 ~ 1990
    0x00e92, 0x00d26, 0x0652e, 0x00a57, 0x10ad6, 0x0035a, 0x006d5, 0x0ab69, 0x00749, 0x00693,  # 1991 ~ 2000
    0x08a9b, 0x0052b, 0x00a5b, 0x04aae, 0x0056a, 0x0edd5, 0x00ba4, 0x00b49, 0x0ad53, 0x00a95,  # 2001 ~ 2010
    0x0052d, 0x0855d, 0x00ab5, 0x12baa, 0x005d2, 0x00da5, 0x0de8a, 0x00d4a, 0x00c95, 0x08a9e,  # 2011 ~ 2020
    0x00556, 0x00ab5, 0x04ada, 0x006d2, 0x0c765, 0x00725, 0x0064b, 0x0a657, 0x00cab, 0x0055a,  # 2021 ~ 2030
    0x0656e, 0x00b69, 0x16f52, 0x00b52, 0x00b25, 0x0dd0b, 0x00a4b, 0x004ab, 0x0a2bb, 0x005ad,  # 2031 ~ 2040
    0x00b6a, 0x04daa, 0x00d92, 0x0eea5, 0x00d25, 0x00a55, 0x0ba4d, 0x004b6, 0x005b5, 0x076d2,  # 2041 ~ 2050
    0x00ec9, 0x10f92, 0x00e92, 0x00d26, 0x0d516, 0x00a57, 0x00556, 0x09365, 0x00755, 0x00749,  # 2051 ~ 2060
    0x0674b, 0x00693, 0x0eaab, 0x0052b, 0x00a5b, 0x0aaba, 0x0056a, 0x00b65, 0x08baa, 0x00b4a,  # 2061 ~ 2070
    0x10d95, 0x00a95, 0x0052d, 0x0c56d, 0x00ab5, 0x005aa, 0x085d5, 0x00da5, 0x00d4a, 0x06e4d,  # 2071 ~ 2080
    0x00c96, 0x0ecce, 0x00556, 0x00ab5, 0x0bad2, 0x006d2, 0x00ea5, 0x0872a, 0x0068b, 0x10697,  # 2081 ~ 2090
    0x004ab, 0x0055b, 0x0d556, 0x00b6a, 0x00752, 0x08b95, 0x00b45, 0x00a8b, 0x04a4f, ]

g_lunar_year_day = [
    0x18d3, 0x1348, 0x0e3d, 0x1750, 0x1144, 0x0c39, 0x15cd, 0x1042, 0x0ab6, 0x144a,  # 1901 ~ 1910
    0x0ebe, 0x1852, 0x1246, 0x0cba, 0x164e, 0x10c3, 0x0b37, 0x14cb, 0x0fc1, 0x1954,  # 1911 ~ 1920
    0x1348, 0x0dbc, 0x1750, 0x11c5, 0x0bb8, 0x15cd, 0x1042, 0x0b37, 0x144a, 0x0ebe,  # 1921 ~ 1930
    0x17d1, 0x1246, 0x0cba, 0x164e, 0x1144, 0x0bb8, 0x14cb, 0x0f3f, 0x18d3, 0x1348,  # 1931 ~ 1940
    0x0d3b, 0x16cf, 0x11c5, 0x0c39, 0x15cd, 0x1042, 0x0ab6, 0x144a, 0x0e3d, 0x17d1,  # 1941 ~ 1950
    0x1246, 0x0d3b, 0x164e, 0x10c3, 0x0bb8, 0x154c, 0x0f3f, 0x1852, 0x1348, 0x0dbc,  # 1951 ~ 1960
    0x16cf, 0x11c5, 0x0c39, 0x15cd, 0x1042, 0x0a35, 0x13c9, 0x0ebe, 0x17d1, 0x1246,  # 1961 ~ 1970
    0x0d3b, 0x16cf, 0x10c3, 0x0b37, 0x14cb, 0x0f3f, 0x1852, 0x12c7, 0x0dbc, 0x1750,  # 1971 ~ 1980
    0x11c5, 0x0c39, 0x15cd, 0x1042, 0x1954, 0x13c9, 0x0e3d, 0x17d1, 0x1246, 0x0d3b,  # 1981 ~ 1990
    0x16cf, 0x1144, 0x0b37, 0x144a, 0x0f3f, 0x18d3, 0x12c7, 0x0dbc, 0x1750, 0x11c5,  # 1991 ~ 2000
    0x0bb8, 0x154c, 0x0fc1, 0x0ab6, 0x13c9, 0x0e3d, 0x1852, 0x12c7, 0x0cba, 0x164e,  # 2001 ~ 2010
    0x10c3, 0x0b37, 0x144a, 0x0f3f, 0x18d3, 0x1348, 0x0dbc, 0x1750, 0x11c5, 0x0c39,  # 2011 ~ 2020
    0x154c, 0x0fc1, 0x0ab6, 0x144a, 0x0e3d, 0x17d1, 0x1246, 0x0cba, 0x15cd, 0x10c3,  # 2021 ~ 2030
    0x0b37, 0x14cb, 0x0f3f, 0x18d3, 0x1348, 0x0dbc, 0x16cf, 0x1144, 0x0bb8, 0x154c,  # 2031 ~ 2040
    0x0fc1, 0x0ab6, 0x144a, 0x0ebe, 0x17d1, 0x1246, 0x0cba, 0x164e, 0x1042, 0x0b37,  # 2041 ~ 2050
    0x14cb, 0x0fc1, 0x18d3, 0x1348, 0x0dbc, 0x16cf, 0x1144, 0x0a38, 0x154c, 0x1042,  # 2051 ~ 2060
    0x0a35, 0x13c9, 0x0e3d, 0x17d1, 0x11c5, 0x0cba, 0x164e, 0x10c3, 0x0b37, 0x14cb,  # 2061 ~ 2070
    0x0f3f, 0x18d3, 0x12c7, 0x0d3b, 0x16cf, 0x11c5, 0x0bb8, 0x154c, 0x1042, 0x0ab6,  # 2071 ~ 2080
    0x13c9, 0x0e3d, 0x17d1, 0x1246, 0x0cba, 0x164e, 0x10c3, 0x0bb8, 0x144a, 0x0ebe,  # 2081 ~ 2090
    0x1852, 0x12c7, 0x0d3b, 0x16cf, 0x11c5, 0x0c39, 0x154c, 0x0fc1, 0x0a35, 0x13c9,  # 2091 ~ 2100
]

# ==================================================================================

from datetime import date, datetime
import calendar

START_YEAR = 1901

month_DAY_BIT = 12
month_NUM_BIT = 13

yuefeng = ["正月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "冬月", "腊月"]
riqi = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
        "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "廿十",
        "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"]

xingqi = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

tiangan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
shengxiao = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]


def change_year(num):
    dx = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    tmp_str = ""
    for i in str(num):
        tmp_str += dx[int(i)]
    return tmp_str


def week_str(tm):
    return xingqi[tm.weekday()]


def lunar_day(day):
    return riqi[(day - 1) % 30]


def lunar_day1(month, day):
    if day == 1:
        return lunar_month(month)
    else:
        return riqi[(day - 1) % 30]


def lunar_month(month):
    leap = (month >> 4) & 0xf
    m = month & 0xf
    month = yuefeng[(m - 1) % 12]
    if leap == m:
        month = "闰" + month
    return month


def lunar_year(year):
    return tiangan[(year - 4) % 10] + dizhi[(year - 4) % 12] + '[' + shengxiao[(year - 4) % 12] + ']'


# 返回：
# a b c
# 闰几月，该闰月多少天 传入月份多少天
def lunar_month_days(lunar_year, lunar_month):
    if (lunar_year < START_YEAR):
        return 30

    leap_month, leap_day, month_day = 0, 0, 0  # 闰几月，该月多少天 传入月份多少天

    tmp = g_lunar_month_day[lunar_year - START_YEAR]

    if tmp & (1 << (lunar_month - 1)):
        month_day = 30
    else:
        month_day = 29

    # 闰月
    leap_month = (tmp >> month_NUM_BIT) & 0xf
    if leap_month:
        if (tmp & (1 << month_DAY_BIT)):
            leap_day = 30
        else:
            leap_day = 29

    return (leap_month, leap_day, month_day)


# 算农历日期
# 返回的月份中，高4bit为闰月月份，低4bit为其它正常月份
def get_ludar_date(tm):
    year, month, day = tm.year, 1, 1
    code_data = g_lunar_year_day[year - START_YEAR]
    days_tmp = (code_data >> 7) & 0x3f
    chunjie_d = (code_data >> 0) & 0x1f
    chunjie_m = (code_data >> 5) & 0x3
    span_days = (tm - datetime(year, chunjie_m, chunjie_d)).days

    # 日期在该年农历之后
    if (span_days >= 0):
        (leap_month, foo, tmp) = lunar_month_days(year, month)
        while span_days >= tmp:
            span_days -= tmp
            if (month == leap_month):
                (leap_month, tmp, foo) = lunar_month_days(year, month)  # 注：tmp变为闰月日数
                if (span_days < tmp):  # 指定日期在闰月中
                    month = (leap_month << 4) | month
                    break
                span_days -= tmp
            month += 1  # 此处累加得到当前是第几个月
            (leap_month, foo, tmp) = lunar_month_days(year, month)
        day += span_days
        return year, month, day
    # 倒算日历
    else:
        month = 12
        year -= 1
        (leap_month, foo, tmp) = lunar_month_days(year, month)
        while abs(span_days) >= tmp:
            span_days += tmp
            month -= 1
            if (month == leap_month):
                (leap_month, tmp, foo) = lunar_month_days(year, month)
                if (abs(span_days) < tmp):  # 指定日期在闰月中
                    month = (leap_month << 4) | month
                    break
                span_days += tmp
            (leap_month, foo, tmp) = lunar_month_days(year, month)
        day += (tmp + span_days)  # 从月份总数中倒扣 得到天数
        return year, month, day


def _show_month(tm):
    (year, month, day) = get_ludar_date(tm)
    print("%d年%d月%d日" % (tm.year, tm.month, tm.day), week_str(tm), end='')
    print("\t农历 %s年 %s年%s%s " % (lunar_year(year), change_year(year), lunar_month(month), lunar_day(day)))  # 根据数组索引确定
    print("一\t\t二\t\t三\t\t四\t\t五\t\t六\t\t日")

    c = calendar.Calendar(0)
    ds = [d for d in c.itermonthdays(tm.year, tm.month)]

    # print(len(ds), ds)
    # 利用calendar直接获取指定年月日期
    count = 0
    for d in ds:
        if d == 0:
            print("\t\t", end='')
            count += 1
            continue

        (year, month, day) = get_ludar_date(datetime(tm.year, tm.month, d))

        if count % 7 == 0:
            print("\n", end='')
        d_str = str(d)
        if d == tm.day:
            d_str = d_str
        print("%s\t" % (d_str + lunar_day1(month, day)), end='')
        count += 1
    print("")

import os
def show_month():
    print('\n\n\n\n\n\n\n\n\n')
    year = u.get()
    month = e.get()
    year = int(year)
    month = int(month)
    day = d.get()
    day = int(day)
    if year > 2100 or year < 1901:
        return
    if month > 13 or month < 1:
        return

    tmp = datetime(year, month, day)
    _show_month(tmp)
def leap_year(year):
    if 0 == year % 4 and 0 != year % 400 or 0 == year % 400:
        return True
    else:
        return False


def get_month_days(year, month):
    days = 31
    if 2 == month:
        if leap_year(year):
            days = 29
        else:
            days = 28
    elif 4 == month or 6 == month or 9 == month or 11 == month:
        days = 30
    return days


def get_total_days(year, month):
    total_days = 0
    for i in range(1, year):
        if leap_year(year):
            total_days += 366
        else:
            total_days += 365
    for i in range(1, month):
        total_days += get_month_days(year, i)
    return total_days
if __name__ == '__main__':
    import tkinter as tk
    window = tk.Tk()
    window.title('万年历')
    window.geometry('450x300')
    tk.Label(window, text='请输入年份:').place(x=50, y=100)
    tk.Label(window, text='请输入月份:').place(x=50, y=140)
    tk.Label(window, text='请输入日期:').place(x=50, y=180)
    u = tk.Entry(window)
    u.place(x=160, y=100)
    e = tk.Entry(window)
    e.place(x=160, y=140)
    d = tk.Entry(window)
    d.place(x=160, y=180)
    bt_login = tk.Button(window, text='开始', command=show_month)
    bt_login.place(x=140, y=230)
    # 主循环
    window.mainloop()