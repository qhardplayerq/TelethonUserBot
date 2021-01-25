import asyncio
import logging
import os
import random
import subprocess
import sys
import time

from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl import functions
from userbot import bot
from sample_config import Config
from userbot.util import admin_cmd, humanbytes, progress, time_formatter

DEL_TIME_OUT = 3
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
                    

@bot.on(admin_cmd(pattern=r"ch ?(.*)"))
async def get_media(event):
    # chat = -1001285905728
    chat = await event.client.get_entity('t.me/joinchat/AAAAAEylXUB6ztFxdgHp1w')
    mesajlar = []
    print("kanaldan rastgele mesaj seçiliyor.")
    await event.edit("kanaldan rastgele link seçiliyor.")
    async for message in bot.iter_messages(chat):
        mesajlar.append(message.id)

    secim = int(random.choice(mesajlar))
#     print(secim)
    x = await bot.forward_messages(
        entity=await event.client.get_entity('https://t.me/deryaaq#1'),
        messages=secim,
        from_peer=await event.client.get_entity('https://t.me/deryaaq#1'),
    )
    await event.edit("kanala başarılı bir şekilde link gönderildi. Kontrol etmek için 👇\n https://t.me/deryaaq#1")
    # x = await bot.get_messages(chat, s)
#     print(x)


@bot.on(admin_cmd(pattern="post ?(.*)"))
async def get_media(event):
    reply_message = await event.get_reply_message()
    k = await event.edit("post gönderildi")
    # print(reply_message)
    if reply_message:
        await event.client.send_message(
            entity=await event.client.get_entity("https://t.me/joinchat/AAAAAEylXUB6ztFxdgHp1w"),#VİP İFŞA +18
            message=reply_message
        )
        
        await asyncio.sleep(1.2)
        await event.client.send_message(
            entity=await event.client.get_entity("https://t.me/joinchat/AAAAAFebp6PIGgUeAC8DWA"),#+18 LİNK İFŞA
            message=reply_message
        )
        
        
       
        
        await asyncio.sleep(1.2)
        await event.client.send_message(
            entity=await event.client.get_entity("https://t.me/joinchat/AAAAAE_oUYlNq2c45oQRlQ"),#PABLO TR
            message=reply_message
        )
        await asyncio.sleep(1.2)
        await event.client.send_message(
            entity=await event.client.get_entity("https://t.me/joinchat/AAAAAEv_bBx6bl0AEojIJA"),#Terbiyesizmisinfbi
            message=reply_message
        )
        await asyncio.sleep(1.2)
        await event.client.send_message(
            entity=await event.client.get_entity("https://t.me/joinchat/AAAAAESgf0f1wctsKPJ0cg"),#SİKSOK OFFİCİAL
            message=reply_message
        )
        await asyncio.sleep(1.2)
        await event.client.send_message(
            entity=await event.client.get_entity("@deryanin_linkleri"),
            message=reply_message
        )
        
        await asyncio.sleep(1.2)
        await event.client.send_message(
            entity=await event.client.get_entity("@deryanin_mekani"),
            message=reply_message
        )
        
      
    #  await asyncio.sleep(1.2)
      #  await event.client.send_message(
          #  entity=await event.client.get_entity("@linkteskilati3"),
          #  message=reply_message
       # )
        
        
        #AHMETİN KANALLARI
       
        
        
                
        
        await asyncio.sleep(1.2)
        # await event.reply(reply_message)
    else:
        await k.edit("mesajı yanıtla lan :)")
#     await k.edit("mesaj tüm kanallara gönderildi")
