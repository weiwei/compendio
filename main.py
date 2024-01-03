import os
from atproto import Client, client_utils
import byg
import jms

text_builder = client_utils.TextBuilder()
text_builder.tag("What is a tag", "anyway")
text_builder.text("📊 流量统计 ")
text_builder.mention("weiweiw.bsky.social", "did:plc:vkrqsz2gz6lhorh52u7luijl")
text_builder.text("\n\n")

post = "📊 流量统计 @weiweiw.bsky.social\n\n"

total1, used1, days_left1 = jms.get_usage()
text_builder.text(f"JMS 月度使用流量: {used1:.2f} GB / {total1:.0f} GB\n")
text_builder.text(f"JMS 距月度重置日: {days_left1} 天\n\n")

total2, used2, days_left2 = byg.get_usage()
text_builder.text(f"BYG 月度使用流量: {used2:.2f} GB / {total2:.0f} GB\n")
text_builder.text(f"BYG 距月度重置日: {days_left2} 天")

client = Client()
client.login('compendio.bsky.social', os.environ['BSKY_PASSWORD'])
client.send_post(text_builder)
