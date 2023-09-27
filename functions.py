from pyrogram import Client, enums
from pyrogram.types import (
InlineKeyboardButton as Button,
InlineKeyboardMarkup as Markup
)



async def clean(bot, chat_id, starting_id):
    message = await bot.get_messages(chat_id, starting_id)
    while not isinstance(message.reply_markup, Markup):
        await bot.delete_messages(chat_id, message.id)
        starting_id-=1
        message = await bot.get_messages(chat_id, starting_id)
    else:
        print(message)
        return True
        
async def get_reply(message, ask_message, digit=False, digit_message="عدد غير صحيح قم بكتابة عدد صحيح", return_type=False, reply_markup=False, return_raw=False):
    if reply_markup != False:
        answer = await message.chat.ask(f"{ask_message}", reply_markup=reply_markup)
    else:
        answer = await message.chat.ask(f"{ask_message}")
        
    if answer.text == "/start" or answer.from_user.is_self:
        return False
        
    if digit:
        while answer.text.isdigit() != True:
            answer = await message.chat.ask(f"{digit_message}")
            if answer.text == "/start" or answer.from_user.is_self:
                return False
            
    if return_type:
        if answer.text.isdigit():
            return int(answer.text)
        else:
            return answer.text
            
    if return_raw:
        return answer
           
    return answer.text
    
    
async def is_admin(bot, chat_id, username):
    try:
        stat = await bot.get_chat_member(chat_id, username)
        if stat.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False