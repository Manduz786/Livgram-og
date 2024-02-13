from chatrobot.plugins.sql.checkuser_sql import get_all_users

@chatbot_cmd("broadcast", is_args=True)
@god_only
async def sedlyfsir(event):
    msgtobroadcast = event.pattern_match.group(1)
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    for starkcast in userstobc:
        try:
            sent_count += 1
            await chatbot.send_message(int(starkcast.chat_id), "<b>You Recived A Broadcast Message 📡</b>", parse_mode="HTML")
            await chatbot.send_message(int(starkcast.chat_id), msgtobroadcast)
            await asyncio.sleep(0.2)
        except Exception as e:
            try:
                logger.info(f"Error : {error_count}\nError : {e} \nUsers : {chat_id}")
            except:
                pass
    await chatbot.send_message(
        event.chat_id,
        f"<b>Broadcast Done in <u>{sent_count}</u> Group/Users and I got <u>{error_count}</u> Error and Total Number Was <u>{len(userstobc)}</u></b>",
        parse_mode="HTML"
    )
    await chatbot.send_message(Config.DUMB_CHAT, f"You BroadCasted A New Message. \nMessage - {msgtobroadcast} \nSent Count - {sent_count}")
