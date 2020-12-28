from userbot import bot
from userbot import tgbot
from userbot.util import admin_cmd
from telethon import events,functions
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os
import asyncio


scheduler = AsyncIOScheduler()

global kont
kont = ""
global knl
knl = ""
global remainder
remainder = ""


@bot.on(admin_cmd(pattern="sfs ?(.*) + ?(.*) + ?(.*)"))
async def dene(event):
    await event.edit("SFS Bitince kaydedilen mesajlara mesaj gelecek.")
    global kont
    global knl
    global remainder
    msg = event.pattern_match.group(1)
    if msg == "on":
        kont = True
        print("kont=True")
        scheduler.add_job(ilk_test, 'interval', seconds=2)
        # scheduler.add_job(ikinci_test, 'interval', seconds=4)
        scheduler.start()
        kanal = event.pattern_match.group(2)
        check = await bot.get_entity(str(kanal))
        knl = check.id
        hatırlat = event.pattern_match.group(3)
        remainder = hatırlat


async def ilk_test():
    global kont
    global knl
    global remainder
    result = await bot(functions.channels.GetFullChannelRequest(
        channel=int(knl)
    ))
    # print(result.stringify())
    print(result.full_chat.participants_count)
    print(remainder)
    if int(result.full_chat.participants_count) == int(remainder):
        await bot.send_message(-1001210735099,"SFS BİTTİ !!!")
        scheduler.shutdown()
        return




