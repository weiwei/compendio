import os
import requests
from utils import get_days_left

SERVICE_ID = os.environ.get("JMS_SERVICE_ID")
URL = f"https://justmysocks5.net/members/getbwcounter.php?service=706401&id={SERVICE_ID}"

def get_usage():
    resp = requests.get(URL)

    data = resp.json()

    total = data["monthly_bw_limit_b"]/1000/1000/1000
    used = data["bw_counter_b"]/1000/1000/1000
    reset_day = data["bw_reset_day_of_month"]
    days_left = get_days_left(reset_day)

    return total, used, days_left

if __name__ == "__main__":
    total, used, days_left = get_usage()
    print(f"JMS: {used:.2f}GB/{total:.2f}GB ({days_left} days left)")

