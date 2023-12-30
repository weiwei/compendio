import os
import requests
from utils import get_days_left

LOGIN_URL = "https://www.bygcloud.com/api/v1/passport/auth/login"
INFO_URL = "https://www.bygcloud.com/api/v1/user/getSubscribe"

EMAIL = os.environ.get("BYG_EMAIL")
PASSWORD = os.environ.get("BYG_PASSWORD")

def get_usage():
    resp = requests.post(json={"email": EMAIL, "password": PASSWORD}, url=LOGIN_URL)

    authorization = resp.json()["data"]["auth_data"]

    resp = requests.get(INFO_URL, headers={"authorization": authorization})

    data = resp.json()["data"]

    total = data["transfer_enable"]/1024/1024/1024
    used = (data["u"] + data["d"])/1024/1024/1024
    reset_day = data["reset_day"]

    return total, used, reset_day

if __name__ == "__main__":
    total, used, reset_day = get_usage()
    days_left = get_days_left(reset_day)
    print(f"BYG: {used:.2f}GB/{total:.2f}GB ({days_left} days left)")
