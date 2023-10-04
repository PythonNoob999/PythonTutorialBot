from pyrogram import Client, filters, types, enums
from pyrogram.types import (
InlineKeyboardMarkup as Markup,
InlineKeyboardButton as Button
)
from utils import (
msg,
keyboards
)
from functions import (
get_reply,
clean,
is_admin
)
from database import DB
import pyromod
import asyncio




bot = Client("PythonTutorialBot", 25299107,"786fa70a24da230b78b3df1fc16a9772", bot_token="6324540456:AAHvmPJD1QZi6DmbZUHYeEw5gUQb62_eo5o")
db = DB()
db.c.execute("SELECT * FROM users")
print(db.c.fetchall())
@bot.on_message(filters.text & filters.private)
async def main_handler(bot, m):
    chat_id = m.chat.id
    text = m.text.split()
    command = text[0].replace("/", "")
    print(text)
    if not db.check_user(m.chat.id):
            lang = await get_reply(m, "Please Choose a Language! | من فضلك قم بإختيار لغة", reply_markup=keyboards["lang"])
            choice = "EN"
            if lang in ["English🇺🇲", "Arabic🇸🇦"]:
                choice = "EN" if lang == "English🇺🇲" else "AR"
            if m.chat.type in [enums.ChatType.SUPERGROUP, enums.ChatType.GROUP]:
                db.add_user(str(m.chat.id), m.chat.username, "GROUP", choice)
            elif m.chat.type == enums.ChatType.PRIVATE:
                db.add_user(str(m.from_user.id), m.from_user.username, "USER", choice)
                
                
    elif command == "start":
        if m.from_user.username == "kerolis55463":
            await bot.send_message(chat_id, "Choose option👇", reply_markup=keyboards["admin"])
        else:            
            lang = db.get_lang(str(m.chat.id))
            if lang == "EN":
                await bot.send_message(chat_id, msg["start-en"], reply_markup=Markup(keyboards["start-en"]))
            elif lang == "AR":
                await bot.send_message(chat_id, msg["start-ar"], reply_markup=Markup(keyboards["start-ar"]))


@bot.on_message(filters.text & filters.group)
async def group_handler(bot, m):
    chat_id = m.chat.id
    text = m.text.split()
    command = ''.join(text).replace("/", "")
    print(command)
    if not db.check_user(m.chat.id):
        db.add_user(str(m.chat.id), m.chat.username, "GROUP", "EN")        
    
    if command == "start":
        lang = db.get_lang(str(m.chat.id))
        if lang == "EN":
            btns = keyboards["start-en"][:]
            btns.pop(-1)
            await bot.send_message(chat_id, msg["start-en"], reply_markup=Markup(btns))
        elif lang == "AR":
            btns = keyboards["start-ar"][:]
            btns.pop(-1)
            await bot.send_message(chat_id, msg["start-ar"], reply_markup=Markup(btns))
            
    elif command.startswith("set_lang_"):
        language = command.split("_")[2]
        if language in ["ar", "en"]:
            if await is_admin(bot, chat_id, m.from_user.username):
                db.update_lang(str(chat_id), language.upper())
                await m.reply_text("✅")
            else:
                await m.reply_text("Chat Admin Required!")
        else:
            await m.reply_text("Unkown Language!")
   
    elif command.startswith("send_private_"):
         status = command.split("_")[2]
         if status.lower() == "on":
             if await is_admin(bot, chat_id, m.from_user.username):
                 db.update_settings(str(m.chat.id), "on")
                 await m.reply_text("✅")
             else:
                 await m.reply_text("Chat Admin Required!")
         elif status.lower() == "off":
             if await is_admin(bot, chat_id, m.from_user.username):
                 db.update_settings(str(m.chat.id), "off")
                 await m.reply_text("✅")
             else:
                 await m.reply_text("Chat Admin Required!")             
         else:
             await m.reply_text("Unkown option!")
         

        

@bot.on_callback_query()
async def handy(bot, CallBack):
    message = CallBack.message
    chat = message.chat.id
    data = CallBack.data
    print(data)
    
    #*/ Admin panel */#
    if data == "make_a_message":
        do_it = False
        sid = 0
        temp_lang = await get_reply(message, "Send template Language!", reply_markup=keyboards["lang"],return_raw=True)
        if temp_lang != False:
            template = msg["template-ar"] if temp_lang.text == "Arabic🇸🇦" else msg["template-en"]
            main_title = await get_reply(message, "Send main title")
            if main_title:
                desc = await get_reply(message, "Send Short Description💬")
                if desc:
                    syntax = await get_reply(message, "Send Syntax⌨️")
                    if syntax:
                        usage_example = await get_reply(message, "Send Usage Example❓")
                        if usage_example:
                            example = await get_reply(message, "Send Example📟:", return_raw=True)
                            if example != False:
                                sid = example.id
                                example = example.text
                                do_it = True
        if do_it:
            await clean(bot, chat, sid)
            await bot.send_message(chat, template.format(main_title, desc, syntax, usage_example, example), parse_mode=enums.ParseMode.DISABLED)

    #*/ User Panel */#
    elif data.startswith("info"):
        lang = db.get_lang(str(chat))
        stat = db.get_type(str(chat))
        material = data.split("-")[1]
        if lang == "EN":
            if stat == "GROUP":
                sending = db.get_settings(str(chat))
                if sending.lower() == "off":
                    await CallBack.edit_message_text(text=msg[f"{material}-en"], reply_markup=keyboards[material])
                elif sending.lower() == "on":
                    try:
                        await bot.send_message(CallBack.from_user.id, msg[f"{material}-en"], reply_markup=keyboards[material])
                        #await bot.send_message(chat, f"sent info to user [{CallBack.from_user.first_name}](tg://user?id={CallBack.from_user.id})")
                    except:
                        pass
                        #await bot.send_message(chat, f"Failed to send info in [{CallBack.from_user.first_name}](tg://user?id={CallBack.from_user.id}) pm")
            elif stat == "USER":
                await CallBack.edit_message_text(text=msg[f"{material}-en"], reply_markup=keyboards[material])
        elif lang == 'AR':
            if stat == "GROUP":
                sending = db.get_settings(str(chat))
                if sending.lower() == "off":
                    await CallBack.edit_message_text(text=msg[f"{material}-en"], reply_markup=keyboards[material])
                elif sending.lower() == "on":
                    try:
                        await bot.send_message(CallBack.from_user.id, msg[f"{material}-en"], reply_markup=keyboards[material])
                        await bot.send_message(chat, f"sent info to user [{CallBack.from_user.first_name}](tg://user?id={CallBack.from_user.id})")
                    except:
                        await bot.send_message(chat, f"Failed to send info in [{CallBack.from_user.first_name}](tg://user?id={CallBack.from_user.id}) pm")                
            elif stat == "USER":
                await CallBack.edit_message_text(text=msg[f"{material}-ar"], reply_markup=keyboards[material])

    elif data in ["data_types-ar", "data_types-en", "loops-ar", "loops-en", "basic_funcs-en", "basic_funcs-ar"]:
        await CallBack.edit_message_text(text=msg[data], reply_markup=keyboards[data])
        
    elif data.startswith('data_types') or data.startswith("loops") or data.startswith("basic_funcs"):
        await CallBack.edit_message_text(text=msg[data], reply_markup=Markup([[Button("↩️", callback_data=f"{data.split('-')[0]}-{data.split('-')[-1]}")]]))
                    
    elif data == "set_lang":
        lang = await get_reply(message, "Please Choose a Language! | من فضلك قم بإختيار لغة", reply_markup=keyboards["lang"], return_raw=True)
        if lang != False:
            if lang.text == 'English🇺🇲':
                db.update_lang(str(chat), "EN")
                await clean(bot, chat, lang.id)                
                await bot.send_message(chat, "Done ✅")
                try:
                    await CallBack.edit_message_text(text=msg["start-en"], reply_markup=Markup(keyboards["start-en"])) 
                except:
                    pass
            elif lang.text == 'Arabic🇸🇦':
                db.update_lang(str(chat), "AR")
                await clean(bot, chat, lang.id)                
                await bot.send_message(chat, "تم ✅")                
                try:
                    await CallBack.edit_message_text(text=msg["start-ar"], reply_markup=Markup(keyboards["start-ar"]))
                except:
                    pass
                 


    elif data == "back":
        lang = db.get_lang(str(chat))
        stat = db.get_type(str(chat))
        if lang == "EN":
            # we pop the last button on the standard keyboard, to prevent any member to change group language
            if stat == "GROUP":
                sending = db.get_settings(str(chat))
                btns = keyboards["start-en"][:]
                btns.pop(-1)
                if sending.lower() == "off":
                    await CallBack.edit_message_text(text=msg["start-en"], reply_markup=Markup(btns))
                elif sending.lower() == "on":
                    try:
                        await bot.send_message(CallBack.from_user.id, msg["start-en"], reply_markup=Markup(keyboards["start-en"]))
                        #await bot.send_message(chat, f"sent info to user [{CallBack.from_user.first_name}](tg://user?id={CallBack.from_user.id})")
                    except:
                        pass
                        #await bot.send_message(chat, f"Failed to send info in [{CallBack.from_user.first_name}](tg://user?id={CallBack.from_user.id}) pm")
            elif stat == "USER":
                await CallBack.edit_message_text(text=msg["start-en"], reply_markup=Markup(keyboards["start-en"]))
        elif lang == "AR":
            if stat == "GROUP":
                sending = db.get_settings(str(chat))
                btns = keyboards["start-ar"][:]     
                btns.pop(-1)         
                if sending.lower() == "off":
                    await CallBack.edit_message_text(text=msg["start-ar"], reply_markup=Markup(btns))
                elif sending.lower() == "on":
                    try:
                        await bot.send_message(CallBack.from_user.id, msg["start-ar"], reply_markup=Markup(keyboards["start-ar"]))
                        #await bot.send_message(chat, f"تم ارسال المعلومات عند  [{CallBack.from_user.first_name}](tg://user?id={CallBack.from_user.id})")
                    except:
                        pass
                        #await bot.send_message(chat, f"فشل ارسال المعلومات الي  [{CallBack.from_user.first_name}](tg://user?id={CallBack.from_user.id}) pm")
                                        
            elif stat == "USER":
                await CallBack.edit_message_text(text=msg["start-ar"], reply_markup=Markup(keyboards["start-ar"]))          






asyncio.run(bot.run())    