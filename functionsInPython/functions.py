import datetime
def currentYear():
    date = datetime.date.today()
    year = date.year
    print(date)
    print(year)
    
currentYear()