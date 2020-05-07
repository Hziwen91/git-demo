from dateutil import rrule
from datetime import datetime
import time
# 第一个github提交
# github调试
# pyinstaller -F C:\Users\TX\Desktop\code\日常小工具\计算时间.py
# 开始年月日
startYear = int(input('请输入要查询的年份：'))
startMonth = int(input('请输入要查询的月份：'))
startDay = int(input('请输入要查询的日期：'))

# 当天年月日
untilYear = int(time.strftime('%Y',time.localtime(time.time())))
untilMonth = int(time.strftime('%m',time.localtime(time.time())))
untilDay = int(time.strftime('%d',time.localtime(time.time())))

# 赋值
firstDay = datetime(startYear, startMonth, startDay)
endDay = datetime(untilYear, untilMonth, untilDay)

# rrule.DAILY计算天差，此外还有  星期(WEEKLY)，年（YEARLY）
days = rrule.rrule(freq=rrule.DAILY, dtstart=firstDay, until=endDay)
print('认识:', days.count(), '天')
time.sleep(5)

# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# 获取当前日期2020-04-07 14:12:27
