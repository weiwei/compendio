import os
from atproto import Client
import byg
import jms
from utils import get_days_left

post = "📊 流量统计 @weiweiw.bsky.social\n\n"

total1, used1, days_left1 = jms.get_usage()

post += f"JMS 月度使用流量: {used1:.2f} GB / {total1:.0f} GB\n"
post += f"JMS 距月度重置日: {days_left1} 天\n\n"

total2, used2, days_left2 = byg.get_usage()

post += f"BYG 月度使用流量: {used2:.2f} GB / {total2:.0f} GB\n"
post += f"BYG 距月度重置日: {days_left2} 天\n"

facets = [{
    "index": {
        "byteStart": 8,
        "byteEnd": 27
    },
    "features": {
        "type": "app.bsky.richtext.facet#mention",
        "did": "did:plc:vkrqsz2gz6lhorh52u7luijl"
    }
}]

client = Client()
client.login('compendio.bsky.social', os.environ['BSKY_PASSWORD'])
client.send_post(text=post, facets=facets)
