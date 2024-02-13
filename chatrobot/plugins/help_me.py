from chatrobot.plugins.sql.users_sql import add_me_in_db, his_userid
from chatrobot.plugins.sql.checkuser_sql import add_usersid_in_db, already_added, get_all_users
from telethon import custom, events, Button
import re
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

@chatbot_cmd("assistant", is_args=False)
async def sedlyfsir(event):
    starkbot = await chatbot.get_me()
    bot_id = starkbot.first_name
    bot_username = starkbot.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    vent = event.chat_id
    oknoob = Config.OWNER_ID
    oksir = Config.CUSTOM_START
    if Config.CUSTOM_START is None:
        text_me = (f"**Hey. {firstname} , I am {bot_username}.** \n"
               f"I am a chatbot to talk with my master \n"
               f"send me message and i will send to my master. \n"
               f"he will reply you soon \n\nthank you")
    else:
        text_me = f"{oksir}"
    formaster = "Sir. How Can I Help You?"
    if event.sender_id == Config.OWNER_ID:
        ok = await chatbot.send_message(event.chat_id, message=formaster, buttons = [
             [custom.Button.inline("Commands For Owner.", data="cmds")],
             [custom.Button.inline("Close", data="close ")],
              ]
             )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
            await chatbot.send_message(Config.DUMB_CHAT, f"NEW USER ! \nUser ID : `{event.chat_id}`")
        await chatbot.send_file(event.chat_id, file=Config.CUSTOM_IMG, caption=text_me, buttons = [
             [custom.Button.inline("About me", data="mewant")],
             [custom.Button.inline("Close", data="close ")],
              ]
             )
    

    
@chatbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"mewant")))
async def help(event):
    if event.query.user_id is not Config.OWNER_ID:
        await event.edit(
            "About help",
            buttons=[
                [Button.url("About", "https://t.me/i_14344")],
                [Button.url("My bot", "t.me/ScenarioXbot")],
            ],
        )
        
@chatbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
async def help(event):
    await event.delete()
              
              
@chatbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"cmds")))
async def help(event):
    msg = (f"<b><u> Commands </b></u> \n<code>➤ /start - Starts Bot \n➤ /block - Reply To User To Block Him \n➤ /unblock - Unblocks A User \n➤ /alive - Am I Alive? \n➤ /broadcast - Broadcasts A Message \n➤ /stats - Show Bot Stats </code>")
    await event.edit(msg, parse_mode="HTML")

#
