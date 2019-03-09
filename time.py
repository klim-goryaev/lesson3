import datetime  #импорт модуля времени
import timedelta #импорт модуля timedelta
import locale  #импорт модуля locale 
locale.setlocale(locale.LC_ALL, "russian")
from datetime import datetime #импортируем datetime
from datetime import timedelta #импортируем timedelta
dt_now = datetime.now() #присваиваем 
delta_day = timedelta(days=1)
dt_yesterday = (dt_now-delta_day)
delta_month = timedelta(days=30)
dt_last_month = (dt_now-delta_month)
print ('Дата вчера: ',dt_yesterday.strftime('%A %d.%m.%Y')) #дата вчера
print ("Дата сегодня: ",dt_now.strftime('%A %d.%m.%Y')) #дата сейчас
print ("Дата месяц назад: ",dt_last_month.strftime('%A %d.%m.%Y')) #дата месяц назад
date_string = '01/01/17 12:10:03.234567'#stirng из примера
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f') #приводим к распознованию
print ("Полное время: ", date_dt) #показываем полную дату
print (date_dt.strftime('%A %d.%m.%Y %H:%M')) #показываем удобную нам дату