import datetime
def currentYear():
    date = datetime.date.today()
    year = datetime.date.year()
    time = datetime.time.time()
    print(date)
    print(year)
    print(time)


currentYear()