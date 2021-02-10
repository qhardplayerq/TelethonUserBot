import json
import logging
import requests
# import aiohttp
import asyncio
from userbot import bot
from userbot.util import admin_cmd
from urllib.request import Request, urlopen
WEB_HDRS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept': 'text/html,text/plain,application/xhtml+xml,application/xml,application/_json;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Charset': 'Windows-1252,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8;q=0.5',
    'Connection': 'keep-alive'
}
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)



@bot.on(admin_cmd(pattern=("kisalt ?(.*)")))
async def get_adzan(event):
  link = event.pattern_match.group(1)
  if link:
      api = f"https://ay.live/st/?api=e2bb35a996ea8c9dfa4e5011005730bb584e283f&url={link}&alias&ct=1"
      req = Request(api, headers=WEB_HDRS)
      web_byte = urlopen(req).read()
      webpage = web_byte.decode('utf-8')
      data = json.loads(webpage)
      await event.edit(data['shortenedUrl'])



                    





  
  
  
      
      
      
      
      







    

