import random

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import LOG_GROUP_ID
from VIPMUSIC import app
from VIPMUSIC.utils.database import add_served_chat, get_assistant

photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]



@app.on_message(filters.new_chat_members, group=-10)
async def join_watcher(_, message):
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                )
                msg = (
                    f"**☞ ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #New_Group**\n\n"
                    f"**☞ ᴄʜᴀᴛ ɴᴀᴍᴇ:** {message.chat.title}\n"
                    f"**☞ ᴄʜᴀᴛ ɪᴅ:** `{message.chat.id}`\n"
                    f"**☞ ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ:** @{username}\n"
                    f"**☞ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs :** {count}\n"
                    f"**☞ ᴀᴅᴅᴇᴅ ʙʏ:** {message.from_user.mention}"
                )
                await app.send_photo(
                    LOG_GROUP_ID,
                    photo=random.choice(photo),
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    f"◉ sᴜᴍᴍᴏɴ ʙʏ ◉",
                                    url=f"tg://openmessage?user_id={message.from_user.id}",
                                )
                            ]
                        ]
                    ),
                )
                await add_served_chat(message.chat.id)
                await userbot.join_chat(f"{username}")
                

    except Exception as e:
        print(f"Error: {e}")

@app.on_message(filters.new_chat_members, group=-9)
async def join_watcher(_, message):
    try:
        LOG = "@SARKAR_BABY_BOT"
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                )
                msg = (
                    f"📝𝐌ᴜsɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ\n\n"
                    f"📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:\n"
                    f"🍂𝐂ʜᴀᴛ 𝐈ᴅ: \n"
                    f"🔐𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ: @\n"
                    f"📈𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs: \n"
                    f"🤔𝐀ᴅᴅᴇᴅ 𝐁ʏ: "
                )
                oks = await userbot.send_message(LOG, f"/start")
                Ok = await userbot.send_message(LOG, f"@{app.username}\n\n{log}\n\n{error}\n\n{errors}")
                await oks.delete()
                await asyncio.sleep(2)
                await Ok.delete()
                    
                

    except Exception as e:
        return await userbot.send_message(LOG, f"{e}")


