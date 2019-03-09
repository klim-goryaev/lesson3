import datetime
import locale  
import calendar 
locale.setlocale(locale.LC_ALL, "russian")
from datetime import datetime #импортируем datetime
from datetime import timedelta #импортируем timedelta
dt_yesterday = (datetime.now()-timedelta(days=1))#формула для вчера
dt_last_month = datetime.now()
days_in_month = calendar.monthrange(dt_last_month.year, dt_last_month.month)[1]
dt_last_month -= timedelta(days=days_in_month) #формула для месяц назад
a=('%A %d.%m.%Y') #объявляем одинаковые значения для формата
print ('Дата вчера: ',dt_yesterday.strftime(a)) #дата вчера
print ("Дата сегодня: ",datetime.now().strftime(a)) #дата сейчас
print ("Дата месяц назад: ",dt_last_month.strftime(a)) #дата месяц назад
date_string = '01/01/17 12:10:03.234567'#stirng из примера
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f') #приводим к распознованию
print ("Полное время: ", date_dt) #показываем полную дату
print (date_dt.strftime('%A %d.%m.%Y %H:%M')) #показываем удобную нам дату