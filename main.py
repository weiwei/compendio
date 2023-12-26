import os
from atproto import Client
import byg
import jms
from utils import get_days_left

post = "📊 流量统计 @weiweiw.bsky.social\n\n"

total1, used1, reset_day1 = jms.get_usage()
days_left1 = get_days_left(reset_day1)

post += f"JMS 月度使用流量: {used1:.2f} GB / {total1:.0f} GB\n"
post += f"JMS 距月度重置日: {days_left1} 天\n\n"

total2, used2, reset_day2 = byg.get_usage()
days_left2 = get_days_left(reset_day2)

post += f"BYG 月度使用流量: {used2:.2f} GB / {total2:.0f} GB\n"
post += f"BYG 距月度重置日: {days_left2} 天\n"

client = Client()
client.login('compendio.bsky.social', os.environ['BSKY_PASSWORD'])
client.send_post(text=post)
