from chatrobot.plugins.sql.blacklist_sql import add_nibba_in_db, get_all_nibba, is_he_added, removenibba
from chatrobot.plugins.sql.users_sql import add_me_in_db, his_userid

@chatbot_cmd("block", is_args=False)
@god_only
async def starkisnoob(event):
    if event.sender_id == Config.OWNER_ID:
        msg = await event.get_reply_message()
        if msg is None:
            await event.reply("Reply To User")
        user_id, reply_message_id = his_userid(msg.id)
    if is_he_added(user_id):
        await event.reply("Already Blacklisted.")
    elif not is_he_added(user_id):
        add_nibba_in_db(user_id)
        await event.reply("Blacklisted This Dumb Person")
        await chatbot.send_message(
            user_id, "You Have Been Blacklisted And You Can't Message My Master Now."
        )
        await chatbot.send_message(Config.DUMB_CHAT, f"Blacklisted New user \nUser ID : {user_id}")

@chatbot_cmd("unblock", is_args=False)
@god_only
async def starky(event):
    if event.sender_id == Config.OWNER_ID:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if not is_he_added(user_id):
        await event.reply("Not Even Blacklisted.")
    elif is_he_added(user_id):
        removenibba(user_id)
        await event.reply("DisBlacklisted This Dumb Person")
        await chatbot.send_message(
            user_id, "Congo! You Have Been Unblacklisted By My Master."
        )
        await chatbot.send_message(Config.DUMB_CHAT, f"DisBlacklisted User \nUser ID : {user_id}")
