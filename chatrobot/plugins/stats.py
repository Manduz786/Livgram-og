from chatrobot.plugins.sql.checkuser_sql import get_all_users

@chatbot_cmd("stats", is_args=False)
@god_only
async def starkisnoob(event):
    starkisnoob = get_all_users()
    await event.reply(f"<b>I have <u>{len(starkisnoob)}</u> Users In Database.😁</b>", parse_mode="HTML")

@chatbot_cmd("alive", is_args=False)
@god_only
async def stark(event):
    await event.reply("<b><u>Yeah, I am Alive.</b></u>", parse_mode="HTML")
