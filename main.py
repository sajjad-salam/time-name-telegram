from datetime import datetime as da
from random import choice as ch
from aiocron import crontab as cr
from pyrogram import Client, idle
from pytz import timezone as time

Z = "\x1b[1;31m"
X = "\x1b[1;33m"
Z1 = "\x1b[2;31m"
F = "\x1b[2;32m"
A = "\x1b[2;34m"
C = "\x1b[2;35m"
BB = "\x1b[2;36m"
Y = "\x1b[1;34m"
all = "_._._._._."
R = "\x1b[1;31m"
G = "\x1b[1;32m"
Y = "\x1b[1;33m"
Bl = "\x1b[1;34m"
P = "\x1b[1;35m"
C = "\x1b[1;36m"
W = "\x1b[1;37m"
E = "\x1b[0;90m"
print(("\033[92m—" * 25) + "\n• DEV BY @S_J_O_D •\n" + ("—" * 25))
print(
    f"""{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-

    𓆩‹ 𝐾𝐼𝑁𝐺 𝑂𝐹 𝐸𝑁𝐺𓆪

                              ███████╗  █████╗       ██╗      ██╗  █████╗  ██████╗  
                              ██╔════╝ ██╔══██╗      ██║      ██║ ██╔══██╗ ██╔══██╗ 
                              ███████╗ ███████║      ██║      ██║ ███████║ ██║  ██║ 
                              ╚════██║ ██╔══██║ ██   ██║ ██   ██║ ██╔══██║ ██║  ██║ 
                              ███████║ ██║  ██║ ╚█████╔╝ ╚█████╔╝ ██║  ██║ ██████╔╝ 
                              ╚══════╝ ╚═╝  ╚═╝  ╚════╝   ╚════╝  ╚═╝  ╚═╝ ╚═════╝  
                  『ᴍᴀᴅᴇ ʙʏ : ENG.DEV SAJJAD ™ 
                         ᴛᴇʟᴇɢʀᴀᴍ: https://t.me/S_J_O_D 
                            DEV-INFO : https://t.me/KING_OF_ENG  』
                            
                            
{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-
  {Y}[{P}*{Y}]{C}Code By :{W} 𓆩𝑬𝑵𝑮-𝑺𝑨𝑱𝑱𝑨𝑫𓆪
  {Y}[{P}*{Y}]{C}DEV-INFO : {W}@KING_OF_ENG
{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-"""
)
dead = C + """▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬~𓆩𝑬𝑵𝑮-𝑺𝑨𝑱𝑱𝑨𝑫𓆪~▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬"""
print(dead)
api_id = input(
    "  \x1b[38;5;117m{\x1b[1;32m•\x1b[38;5;117m}  \x1b[38;5;180m ᴀᴘɪ ɪᴅ )  \x1b[1;38;5;121m ๛   \x1b[38;5;117m"
)
api_hash = input(
    "  \x1b[38;5;117m{\x1b[1;32m•\x1b[38;5;117m}  \x1b[38;5;180m ᴀᴘɪ ʜᴀsʜ )  \x1b[1;38;5;121m ๛   \x1b[38;5;117m"
)
phone_number = input(
    "  \x1b[38;5;117m{\x1b[1;32m•\x1b[38;5;117m}  \x1b[38;5;180m ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ )  \x1b[1;38;5;121m ๛   \x1b[38;5;117m"
)

time_zone, fonts = time("Asia/Baghdad"), [
    ["𝟘", "𝟙", "𝟚", "𝟛", "𝟜", "𝟝", "𝟞", "𝟟", "𝟠", "𝟡"],
    ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
    ["⓪", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨"],
    ["𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"],
]
app = Client("Dev_pyc", api_id, api_hash, phone_number=phone_number)


@cr("*/1 * * * *", tz=time_zone, start=False)
async def change_name():
    table = str.maketrans("0123456789", "".join(ch(fonts)))
    time, biot = da.now(time_zone).strftime("%I:%M"), "Golden > {}"
    await app.update_profile(
        last_name=time.translate(table), bio=biot.format(time.translate(table))
    )


app.start(), change_name.start(), idle(), change_name.stop(), app.stop()
