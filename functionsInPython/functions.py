import datetime
#general date time
def currentYear():
    date = datetime.date.today()
    year = date.year
    print(date)
    print(year)

    now = datetime.datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    print("Current Time:", currentTime)
currentYear()


from datetime import date

# date object of today's date
def dayMonthYear():
    today = date.today() 
    print("Current year:", today.year)
    print("Current month:", today.month)
    print("Current day:", today.day)
dayMonthYear()


#local timezone