from datetime import datetime as da
from random import choice as ch
from aiocron import crontab as cr
from pyrogram import Client, idle
from pytz import timezone as time
api_id,api_hash,phone_number = 'ايبي ايدي', "ايبي هاش","+964 رقمك" # رقم 
time_zone,fonts = time("Asia/Baghdad"),[["𝟘", "𝟙", "𝟚", "𝟛", "𝟜", "𝟝", "𝟞", "𝟟", "𝟠", "𝟡"],["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],["⓪","①","②","③","④","⑤","⑥","⑦","⑧","⑨"],["𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"],]
app = Client("Dev_pyc",api_id,api_hash,phone_number=phone_number)
@cr("*/1 * * * *", tz=time_zone, start=False)
async def change_name():
    table = str.maketrans("0123456789", "".join(ch(fonts)))
    time,biot = da.now(time_zone).strftime("%I:%M"),"Golden > {}"
    await app.update_profile(last_name=time.translate(table),bio=biot.format(time.translate(table)))
app.start(),change_name.start(),idle(),change_name.stop(),app.stop()