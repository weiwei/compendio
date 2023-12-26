import os
import requests

SERVICE_ID = os.environ.get("JMS_SERVICE_ID")
URL = f"https://justmysocks5.net/members/getbwcounter.php?service=706401&id={SERVICE_ID}"

def get_usage():
    resp = requests.get(URL)

    data = resp.json()

    total = data["monthly_bw_limit_b"]/1000/1000/1000
    used = data["bw_counter_b"]/1000/1000/1000
    reset_day = data["bw_reset_day_of_month"]

    return total, used, reset_day

