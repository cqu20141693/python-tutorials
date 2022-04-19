chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
"""
cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0
    """
cz_num = {i: 0 for i in chinese_zodiac}  # 字典推导式 i是key 看起来更加简洁
"""
z_num = {}
for i in zodiac_name:
    z_num[i] = 0
    """
z_num = {i: 0 for i in zodiac_name}
while True:
    int_year = int(input('请输入的年份：'))
    int_month = int(input('请输入你的月份：'))
    int_day = int(input('请输入你的日期：'))
    for zd_num in range(len(zodiac_days)):
        if zodiac_days[zd_num] >= (int_month, int_day):
            print(zodiac_name[zd_num])
            break  # 为了得到之后跳出整个循环
        elif int_month == 12 and int_day > 23:
            print(zodiac_name[0])  # 对星座进行输出
            break
    print('%s 年的生肖是 %s' % (int_year, chinese_zodiac[int_year % 12]))
    cz_num[chinese_zodiac[int_year % 12]] += 1
    z_num[zodiac_name[zd_num]] += 1  # key值加一
    for each_key in cz_num.keys():  # 统计成表
        print('生肖 %s 有 %d 个' % (each_key, cz_num[each_key]))
    for each_key in z_num.keys():
        print('星座 %s 有 %d 个' % (each_key, z_num[each_key]))  # 用来统计出现的次数
    """  
n = 0
while zodiac_days[n] < (int_month,int_day):
       if int_month == 12 and int_days > 23:
         break
         n +=1
print(zodiac_names[n])    
"""