from datetime import datetime, timedelta

def expiry_time_func():
    obj = datetime.now() + timedelta(days = 1)
    return obj
