import datetime

x = datetime.datetime.now()
nowString = str(x.year) + str(x.month) + str(x.day) + '-' + str(x.hour) + str(x.minute) + str(x.second) + '.txt'
print(nowString)
