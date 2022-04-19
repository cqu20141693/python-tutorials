# 输某年某月某日，判断这是一年的第几天？
#  以3月5号为例：这是今年的31+28+5=64天
year = int(input('请输入今年：'))
month = int(input('请输入月份：'))
day = int(input('请输入天数：'))
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    tep = months[month - 1]
else:
    pass
tep += day
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    if month > 2:
        tep += 1
print('%s 年的第 %d 天' % (year, tep))
