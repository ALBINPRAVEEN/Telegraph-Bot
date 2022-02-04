import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Webot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Webot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Webot.send_message(
               chat_id=message.chat.id,
               text="""<b>Hey There, I'm Telegraph Bot

I can upload photos or videos to telegraph. Made by @i_am_albin_praveen  

Hit help button to find out more about how to use me</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Help", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Channel", url="https://t.me/musicwithalby")
                                    ],[
                                      InlineKeyboardButton(
                                            "Developer", url="https://t.me/i_am_albin_praveen")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Webot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Webot.send_message(
               chat_id=message.chat.id,
               text="""<b>Telegraph Bot Help!

Just send a photo or video less than 5mb file size, I'll upload it to telegraph.

~ @musicwithalby</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "Developer", url="https://t.me/i_am_albin_praveen")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Webot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Webot.send_message(
               chat_id=message.chat.id,
               text="""<b>About Telegraph Bot!</b>

<b>♞ owner:</b> <a href="https://t.me/i_am_albin_praveen">Albin </a>

<b>♞ Support:</b> <a href="https://t.me/musicwithalby">Alby BOT Support </a>


<b>~ @musicwithalby</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Webot.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Photo size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin @musicwithalby**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Webot.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Video size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin @musicwithalby**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Webot.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}\n\nJoin @musicwithalby**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Webot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Bot Started!
Join @musicwithalby
"""
)

Webot.run()
