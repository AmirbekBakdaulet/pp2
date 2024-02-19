from datetime import datetime
def diff(d1,d2):
    print(abs(((d1.day-d2.day) + (d1.month-d2.month) *30 + (d1.year-d2.year) *30 *12)*24*3600))
date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")
d1=datetime.strptime(date1,"%Y-%m-%d")
d2=datetime.strptime(date2, "%Y-%m-%d")
diff(d1,d2)