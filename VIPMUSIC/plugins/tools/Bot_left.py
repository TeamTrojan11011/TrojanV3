import random

from pyrogram import filters
from pyrogram.types import Message

from config import LOG_GROUP_ID
from VIPMUSIC import app
from VIPMUSIC.utils.database import delete_served_chat, get_assistant

photo = [
    "https://i.ibb.co/VTX2gb2/photo-2024-09-22-18-12-08-7417534719216058384.jpg",
    "https://i.ibb.co/hLww4Bb/photo-2024-09-22-18-12-13-7417534938259390492.jpg",
    "https://i.ibb.co/89YzpFw/photo-2024-09-22-18-24-57-7417535303331610668.jpg",
    "https://i.ibb.co/bJVY4kD/photo-2024-09-22-18-24-59-7417535440770564100.jpg",
    "https://i.ibb.co/H701nRv/photo-2024-09-22-18-26-37-7417535655518928944.jpg",
]


@app.on_message(filters.left_chat_member, group=-12)
async def on_left_chat_member(_, message: Message):
    try:
        userbot = await get_assistant(message.chat.id)

        left_chat_member = message.left_chat_member
        if left_chat_member and left_chat_member.id == (await app.get_me()).id:
            remove_by = (
                message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
            )
            title = message.chat.title
            username = (
                f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
            )
            chat_id = message.chat.id
            left = f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
            await delete_served_chat(chat_id)
            await userbot.leave_chat(chat_id)
    except Exception as e:
        return
