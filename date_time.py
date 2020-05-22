from datetime import datetime, timedelta，date

today = date.today()
print("Today's date:", today)
today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)


nowtime = datetime.now()    # 现在的时间
nowtime
#datetime.datetime(2017, 6, 20, 20, 11, 12, 926763)
lasthour = datetime(2017, 6, 20, 19, 11, 12, 926763)    # 1个小时前的时间
lasthour
#datetime.datetime(2017, 6, 20, 19, 11, 12, 926763)
lasthour_str = str(lasthour)          # 模拟从数据库取出来的str类型时间数据

#str时间数据转换：
# 将str类型时间数据转换为datetime.datetime类型时间数据
lasthour_new = datetime.strptime(lasthour_str, '%Y-%m-%d %H:%M:%S.%f')
#datetime.datetime(2017, 6, 20, 19, 11, 12, 926763)

#时间比较：
# lasthour_new和nowtime的时间差是否大于1个小时
nowtime - lasthour_new > timedelta(hours=1)
False
# lasthour_new和nowtime的时间差是否等于1个小时
nowtime - lasthour_new == timedelta(hours=1)
True
# lasthour_new和nowtime的时间差是否大于60分钟
nowtime - lasthour_new > timedelta(minutes=60)
False
# lasthour_new和nowtime的时间差是否等于60分钟
nowtime - lasthour_new == timedelta(minutes=60)
True