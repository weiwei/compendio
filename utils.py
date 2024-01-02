from datetime import datetime, date, timedelta
from dateutil import relativedelta

def get_days_left(reset_day: int):
    today = date.today()

    this_month_reset_day = today.replace(day=reset_day)
    next_month_reset_day = (today + relativedelta.relativedelta(months=1)).replace(day=reset_day)
    if today >= this_month_reset_day:
        delta = next_month_reset_day - today
    else:
        delta = this_month_reset_day - today

    return delta.days
