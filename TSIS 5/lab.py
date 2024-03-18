from datetime import datetime, timedelta
x=datetime.now()
y=x -  timedelta(days=5)
print(f"the date:{y}")