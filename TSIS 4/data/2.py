from datetime import datetime, timedelta
x=datetime.now()
y=x-timedelta(days=1)
z=x+timedelta(days=1)
print(y.strftime("%A"), x.strftime("%A"), z.strftime("%A"))