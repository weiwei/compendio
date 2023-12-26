from datetime import datetime, timedelta

def get_days_left(reset_day: int):
    today = datetime.now()

    if today.day >= reset_day:
        next_reset_day = (today.replace(day=1) + timedelta(days=32)).replace(day=reset_day)
    else:
        next_reset_day = today.replace(day=reset_day)

    left = next_reset_day - today

    return left.days
