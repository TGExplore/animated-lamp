from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


HELP_TEXT = """
Hi {}. Welcome to Screenshot Generator Bot. You can use me to generate

    1. Screenshots.
    2. Sample Video.
    3. Trim Video.
  
    IF YOU WANT TO USE ME TO SUBSCRIBE @Zee_Keralam_HD

👉Contact @Cristiano_R0naldo_7"""


@ScreenShotBot.on_message(Filters.private & Filters.command("help"))
async def help(c, m):
    
    await m.reply_text(
        text=HELP_TEXT.format(m.from_user.first_name),
        quote=True
    )
